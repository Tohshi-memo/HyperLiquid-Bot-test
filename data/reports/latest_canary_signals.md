# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T04:30:28.943987+00:00`
- Correlation status: `ready`
- Asset price records: `233`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2042` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.8547` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.1143` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0124` n `7`; crypto_alt avg `0.06` n `223`; crypto_major avg `0.1671` n `7`; equity avg `-0.0786` n `42`; fx avg `0.0176` n `4`; index avg `0.0027` n `9`; metal avg `-0.0207` n `7`; unknown avg `0.0757` n `314`
- 1h: commodity avg `-0.0103` n `7`; crypto_alt avg `0.5101` n `223`; crypto_major avg `0.6866` n `7`; equity avg `-0.1299` n `42`; fx avg `-0.0777` n `4`; index avg `0.071` n `9`; metal avg `-0.004` n `7`; unknown avg `-0.0798` n `314`
- 4h: commodity avg `-0.0848` n `7`; crypto_alt avg `2.7943` n `223`; crypto_major avg `3.1194` n `7`; equity avg `1.0051` n `42`; fx avg `-0.0347` n `4`; index avg `0.6411` n `9`; metal avg `0.2647` n `7`; unknown avg `0.4251` n `314`
- 24h: commodity avg `0.0385` n `7`; crypto_alt avg `2.9354` n `223`; crypto_major avg `3.2429` n `7`; equity avg `1.1197` n `42`; fx avg `-0.0559` n `4`; index avg `0.8871` n `9`; metal avg `0.3468` n `7`; unknown avg `0.644` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3971`, n `225`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3865`, n `225`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3661`, n `229`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3505`, n `229`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2049`, n `225`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1989`, n `229`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.195`, n `225`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1845`, n `229`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1791`, n `229`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1718`, n `225`, weak_sample_signal
