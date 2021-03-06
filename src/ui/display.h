#ifndef UI_DISPLAY_H_
#define UI_DISPLAY_H_

#include "hw/lcd/fbdev.h"
#include "localization/coneslam/localize.h"

class UIDisplay {
 public:
  enum DisplayMode { TRACKMAP = 0, CAMERAVIEW, FRONTVIEW, NUM_MODES };

  bool Init();

#if 0
  void UpdateBirdseye(const uint8_t *yuv, int w, int h);

  void UpdateConeView(const uint8_t *yuv, int ncones, int *conesx);

  void UpdateParticleView(const coneslam::Localizer *l);
#endif

  void UpdateCameraView(const uint8_t *yuv);

  void UpdateCeiltrackView(const float *xytheta, float xgrid, float ygrid,
                           float sixz, float sizy, const int32_t *obs1,
                           const int32_t *obs2, float wheel_v);

  void UpdateConfig(const char *configmenu[], int nconfigs, int config_item,
                    const int16_t *config_values);

  void UpdateEncoders(uint16_t *wheel_pos);
  void UpdateStatus(const char *status, uint16_t color = 0xffff);

  void NextMode();

  uint16_t *GetScreenBuffer() { return screen_.GetBuffer(); }

 private:
  void remapYUV(const uint16_t *maptbl, const uint8_t *yuv, uint16_t *buf);

  LCDScreen screen_;
  uint8_t *backgroundyuv_;
  uint16_t *frontremap_;
  DisplayMode mode_;

  uint16_t configbuf_[100 * 320];
  uint16_t statusbuf_[20 * 320];
};

#endif  // UI_DISPLAY_H_
