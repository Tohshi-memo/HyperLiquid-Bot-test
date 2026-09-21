# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T16:53:06.668548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0331` n `12`; crypto_alt avg `0.2045` n `234`; crypto_major avg `0.417` n `8`; equity avg `0.0953` n `140`; fx avg `-0.0045` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0599` n `20`; unknown avg `0.1824` n `942`
- 1h: commodity avg `-0.1832` n `12`; crypto_alt avg `-0.2152` n `234`; crypto_major avg `-0.4429` n `8`; equity avg `0.0204` n `140`; fx avg `-0.0171` n `6`; index avg `0.0253` n `26`; metal avg `-0.0282` n `20`; unknown avg `27.3399` n `928`
- 4h: commodity avg `-0.3649` n `12`; crypto_alt avg `-0.2647` n `234`; crypto_major avg `0.7206` n `8`; equity avg `0.8235` n `140`; fx avg `-0.0184` n `6`; index avg `0.2277` n `26`; metal avg `-0.2372` n `20`; unknown avg `32.9324` n `870`
- 24h: commodity avg `-1.1814` n `12`; crypto_alt avg `4.2686` n `234`; crypto_major avg `4.8707` n `8`; equity avg `2.6515` n `140`; fx avg `-0.1152` n `6`; index avg `0.5726` n `26`; metal avg `-0.0316` n `20`; unknown avg `13.5748` n `731`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
