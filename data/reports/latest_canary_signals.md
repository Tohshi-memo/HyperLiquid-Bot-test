# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T08:07:35.069562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1229` n `13`; crypto_alt avg `0.0396` n `239`; crypto_major avg `0.105` n `8`; equity avg `-0.1332` n `162`; fx avg `0.0024` n `6`; index avg `-0.0089` n `27`; metal avg `-0.0534` n `20`; unknown avg `0.0769` n `1194`
- 1h: commodity avg `0.0279` n `13`; crypto_alt avg `0.025` n `239`; crypto_major avg `-0.2561` n `8`; equity avg `-0.1332` n `162`; fx avg `0.0154` n `6`; index avg `-0.0078` n `27`; metal avg `-0.1095` n `20`; unknown avg `0.656` n `1194`
- 4h: commodity avg `0.0336` n `13`; crypto_alt avg `1.8072` n `239`; crypto_major avg `0.7246` n `8`; equity avg `-0.0905` n `162`; fx avg `0.0574` n `6`; index avg `-0.0023` n `27`; metal avg `-0.2627` n `20`; unknown avg `3.8877` n `1162`
- 24h: commodity avg `0.5568` n `13`; crypto_alt avg `-0.7648` n `239`; crypto_major avg `-3.3295` n `8`; equity avg `-1.1622` n `162`; fx avg `-0.0333` n `6`; index avg `0.0413` n `27`; metal avg `-0.5997` n `20`; unknown avg `102.7659` n `1093`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
