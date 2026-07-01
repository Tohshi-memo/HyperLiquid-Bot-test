# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T07:52:26.292167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0335` n `12`; crypto_alt avg `0.0221` n `228`; crypto_major avg `0.0738` n `8`; equity avg `0.0346` n `88`; fx avg `0.0165` n `6`; index avg `0.0034` n `23`; metal avg `0.0364` n `20`; unknown avg `-0.0143` n `765`
- 1h: commodity avg `0.0495` n `12`; crypto_alt avg `-0.0201` n `228`; crypto_major avg `0.044` n `8`; equity avg `-0.123` n `88`; fx avg `-0.0036` n `6`; index avg `-0.01` n `23`; metal avg `0.0398` n `20`; unknown avg `-0.0486` n `763`
- 4h: commodity avg `-0.1178` n `12`; crypto_alt avg `-0.731` n `228`; crypto_major avg `-0.9222` n `8`; equity avg `-0.4067` n `88`; fx avg `-0.0253` n `6`; index avg `-0.0942` n `23`; metal avg `-0.1104` n `20`; unknown avg `0.1299` n `743`
- 24h: commodity avg `-0.0974` n `12`; crypto_alt avg `-0.8303` n `228`; crypto_major avg `-0.7006` n `8`; equity avg `0.3361` n `88`; fx avg `0.071` n `6`; index avg `-0.0216` n `23`; metal avg `-0.8117` n `20`; unknown avg `-0.2994` n `743`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
