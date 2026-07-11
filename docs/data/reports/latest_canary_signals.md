# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T14:07:24.418752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.0056` n `230`; crypto_major avg `0.0691` n `8`; equity avg `-0.0468` n `92`; fx avg `-0.0222` n `6`; index avg `-0.0034` n `25`; metal avg `-0.0173` n `20`; unknown avg `-0.008` n `765`
- 1h: commodity avg `-0.0472` n `12`; crypto_alt avg `0.126` n `230`; crypto_major avg `0.1768` n `8`; equity avg `-0.0168` n `92`; fx avg `-0.021` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0144` n `20`; unknown avg `-0.0053` n `765`
- 4h: commodity avg `0.0093` n `12`; crypto_alt avg `0.4648` n `230`; crypto_major avg `0.4115` n `8`; equity avg `-0.1044` n `92`; fx avg `-0.0278` n `6`; index avg `-0.0091` n `25`; metal avg `-0.0276` n `20`; unknown avg `-0.1565` n `765`
- 24h: commodity avg `0.1498` n `12`; crypto_alt avg `0.5097` n `229`; crypto_major avg `-0.0071` n `8`; equity avg `0.1034` n `92`; fx avg `-0.0415` n `6`; index avg `0.0954` n `25`; metal avg `0.0381` n `20`; unknown avg `2.972` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
