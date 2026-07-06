# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T07:52:32.308405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1554` n `12`; crypto_alt avg `0.0387` n `229`; crypto_major avg `0.0229` n `8`; equity avg `0.0274` n `88`; fx avg `-0.0084` n `6`; index avg `0.0165` n `25`; metal avg `0.1199` n `20`; unknown avg `0.0618` n `765`
- 1h: commodity avg `-0.267` n `12`; crypto_alt avg `0.2956` n `229`; crypto_major avg `0.2216` n `8`; equity avg `-0.0144` n `88`; fx avg `-0.0099` n `6`; index avg `0.0205` n `25`; metal avg `0.3085` n `20`; unknown avg `0.1176` n `765`
- 4h: commodity avg `-0.0499` n `12`; crypto_alt avg `-0.4737` n `229`; crypto_major avg `-0.1787` n `8`; equity avg `0.3112` n `88`; fx avg `0.0132` n `6`; index avg `0.1579` n `25`; metal avg `0.2268` n `20`; unknown avg `-0.1313` n `731`
- 24h: commodity avg `-0.3105` n `12`; crypto_alt avg `-0.0856` n `229`; crypto_major avg `0.8703` n `8`; equity avg `-0.6462` n `88`; fx avg `0.0803` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0173` n `20`; unknown avg `1.1742` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
