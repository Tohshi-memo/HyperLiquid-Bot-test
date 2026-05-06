# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T00:00:33.923880+00:00`
- Correlation status: `ready`
- Asset price records: `404`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.052` n `7`; crypto_alt avg `0.1529` n `223`; crypto_major avg `0.0419` n `7`; equity avg `0.0184` n `47`; fx avg `-0.1726` n `4`; index avg `-0.0096` n `6`; metal avg `0.0368` n `7`; unknown avg `0.1695` n `313`
- 1h: commodity avg `-0.2005` n `7`; crypto_alt avg `-0.0738` n `223`; crypto_major avg `-0.3961` n `7`; equity avg `-0.2043` n `47`; fx avg `-0.1479` n `4`; index avg `-0.048` n `6`; metal avg `0.3505` n `7`; unknown avg `-0.3724` n `313`
- 4h: commodity avg `-0.6857` n `7`; crypto_alt avg `0.2517` n `223`; crypto_major avg `-0.2523` n `7`; equity avg `0.8602` n `47`; fx avg `-0.0442` n `4`; index avg `0.3096` n `6`; metal avg `0.82` n `7`; unknown avg `-0.1517` n `313`
- 24h: commodity avg `-1.7959` n `7`; crypto_alt avg `2.2384` n `223`; crypto_major avg `2.3554` n `7`; equity avg `3.0321` n `47`; fx avg `-0.0789` n `4`; index avg `1.8681` n `6`; metal avg `1.4799` n `7`; unknown avg `1.1548` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1926`, n `400`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1863`, n `400`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `400`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1258`, n `400`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1101`, n `400`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1074`, n `396`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.102`, n `400`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `400`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `400`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0998`, n `396`, weak_sample_signal
