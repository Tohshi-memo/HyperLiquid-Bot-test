# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T21:27:28.515269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `-0.0422` n `231`; crypto_major avg `-0.0111` n `8`; equity avg `-0.0381` n `127`; fx avg `0.0012` n `6`; index avg `0.0054` n `26`; metal avg `-0.0255` n `20`; unknown avg `0.1465` n `793`
- 1h: commodity avg `0.0172` n `12`; crypto_alt avg `-0.0735` n `231`; crypto_major avg `0.0101` n `8`; equity avg `-0.0081` n `127`; fx avg `-0.0309` n `6`; index avg `0.0152` n `26`; metal avg `0.0209` n `20`; unknown avg `0.0195` n `793`
- 4h: commodity avg `0.0488` n `12`; crypto_alt avg `-0.52` n `231`; crypto_major avg `-0.9362` n `8`; equity avg `-0.0373` n `127`; fx avg `-0.0487` n `6`; index avg `-0.0045` n `26`; metal avg `-0.1891` n `20`; unknown avg `-0.4563` n `793`
- 24h: commodity avg `-0.0917` n `12`; crypto_alt avg `-3.4286` n `231`; crypto_major avg `-3.6781` n `8`; equity avg `-2.1811` n `127`; fx avg `-0.1417` n `6`; index avg `-0.1811` n `26`; metal avg `-0.3731` n `20`; unknown avg `-0.6367` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
