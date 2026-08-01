# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T09:37:30.618599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `-0.0095` n `230`; crypto_major avg `-0.0058` n `8`; equity avg `-0.0105` n `102`; fx avg `-0.0132` n `6`; index avg `0.0146` n `25`; metal avg `-0.0071` n `20`; unknown avg `-0.0191` n `781`
- 1h: commodity avg `-0.0182` n `12`; crypto_alt avg `-0.0451` n `230`; crypto_major avg `-0.0257` n `8`; equity avg `-0.0818` n `102`; fx avg `-0.0137` n `6`; index avg `-0.0068` n `25`; metal avg `-0.0177` n `20`; unknown avg `-0.0272` n `781`
- 4h: commodity avg `0.036` n `12`; crypto_alt avg `-0.2959` n `230`; crypto_major avg `-0.1708` n `8`; equity avg `0.077` n `102`; fx avg `-0.0051` n `6`; index avg `0.0274` n `25`; metal avg `0.0133` n `20`; unknown avg `-0.0196` n `765`
- 24h: commodity avg `0.6245` n `12`; crypto_alt avg `0.43` n `230`; crypto_major avg `-1.0115` n `8`; equity avg `-2.5464` n `102`; fx avg `-0.0361` n `6`; index avg `-0.282` n `25`; metal avg `-0.0034` n `20`; unknown avg `4.8345` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1076`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1038`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0907`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0742`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0684`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0682`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0647`, n `669`, weak_sample_signal
