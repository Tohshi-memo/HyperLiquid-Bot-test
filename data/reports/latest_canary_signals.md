# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T08:07:30.363350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0246` n `12`; crypto_alt avg `-0.0354` n `228`; crypto_major avg `-0.1658` n `8`; equity avg `-0.014` n `86`; fx avg `-0.0056` n `6`; index avg `-0.0092` n `23`; metal avg `-0.0277` n `20`; unknown avg `-0.005` n `765`
- 1h: commodity avg `-0.1496` n `12`; crypto_alt avg `0.2076` n `228`; crypto_major avg `0.1766` n `8`; equity avg `0.1051` n `86`; fx avg `0.011` n `6`; index avg `0.016` n `23`; metal avg `-0.0221` n `20`; unknown avg `0.0296` n `765`
- 4h: commodity avg `-0.0563` n `12`; crypto_alt avg `1.0671` n `228`; crypto_major avg `1.236` n `8`; equity avg `0.5607` n `86`; fx avg `-0.0714` n `6`; index avg `0.1391` n `23`; metal avg `0.546` n `20`; unknown avg `0.3038` n `733`
- 24h: commodity avg `0.0174` n `12`; crypto_alt avg `-1.5003` n `228`; crypto_major avg `-1.3853` n `8`; equity avg `-3.7825` n `86`; fx avg `0.0257` n `6`; index avg `-0.5389` n `23`; metal avg `0.3863` n `20`; unknown avg `0.6109` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1861`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
