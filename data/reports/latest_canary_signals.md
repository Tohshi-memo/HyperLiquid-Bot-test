# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T04:00:36.575941+00:00`
- Correlation status: `ready`
- Asset price records: `231`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.4098` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.2795` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0027` n `7`; crypto_alt avg `0.3467` n `223`; crypto_major avg `0.3966` n `7`; equity avg `-0.0013` n `42`; fx avg `0.0618` n `4`; index avg `0.0816` n `9`; metal avg `-0.0213` n `7`; unknown avg `-0.0913` n `314`
- 1h: commodity avg `0.0709` n `7`; crypto_alt avg `0.1581` n `223`; crypto_major avg `0.2457` n `7`; equity avg `-0.0473` n `42`; fx avg `-0.0084` n `4`; index avg `0.067` n `9`; metal avg `0.0156` n `7`; unknown avg `-0.1411` n `314`
- 4h: commodity avg `0.0914` n `7`; crypto_alt avg `2.1643` n `223`; crypto_major avg `2.3709` n `7`; equity avg `1.1405` n `42`; fx avg `0.0262` n `4`; index avg `0.6257` n `9`; metal avg `-0.0389` n `7`; unknown avg `0.1991` n `314`
- 24h: commodity avg `0.1474` n `7`; crypto_alt avg `2.8299` n `223`; crypto_major avg `2.9237` n `7`; equity avg `1.1916` n `42`; fx avg `0.0049` n `4`; index avg `0.8443` n `9`; metal avg `0.3227` n `7`; unknown avg `0.5865` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3984`, n `223`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3883`, n `223`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.366`, n `227`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3504`, n `227`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2132`, n `223`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1984`, n `223`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.194`, n `227`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.188`, n `227`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1824`, n `227`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.141`, n `227`, weak_sample_signal
