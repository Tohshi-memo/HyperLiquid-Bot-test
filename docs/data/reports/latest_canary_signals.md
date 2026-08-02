# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T23:24:16.857159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0461` n `12`; crypto_alt avg `0.0688` n `230`; crypto_major avg `0.0806` n `8`; equity avg `-0.026` n `102`; fx avg `0.0597` n `6`; index avg `-0.0153` n `25`; metal avg `0.0253` n `20`; unknown avg `-0.024` n `784`
- 1h: commodity avg `0.0991` n `12`; crypto_alt avg `-0.3662` n `230`; crypto_major avg `-0.4352` n `8`; equity avg `0.0977` n `102`; fx avg `0.0109` n `6`; index avg `0.0383` n `25`; metal avg `-0.0127` n `20`; unknown avg `0.1142` n `783`
- 4h: commodity avg `-0.0239` n `12`; crypto_alt avg `-0.0885` n `230`; crypto_major avg `0.0985` n `8`; equity avg `0.2805` n `102`; fx avg `0.1351` n `6`; index avg `0.0602` n `25`; metal avg `-0.0804` n `20`; unknown avg `1.164` n `783`
- 24h: commodity avg `-1.2505` n `12`; crypto_alt avg `1.1665` n `230`; crypto_major avg `1.6543` n `8`; equity avg `1.6606` n `102`; fx avg `0.0544` n `6`; index avg `0.3519` n `25`; metal avg `0.2052` n `20`; unknown avg `1.607` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
