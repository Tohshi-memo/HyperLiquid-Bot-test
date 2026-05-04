# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T04:45:43.725912+00:00`
- Correlation status: `ready`
- Asset price records: `234`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.1135` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.0009` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.1832` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0211` n `7`; crypto_alt avg `0.0696` n `223`; crypto_major avg `0.1192` n `7`; equity avg `0.0262` n `42`; fx avg `0.0011` n `4`; index avg `-0.0137` n `9`; metal avg `-0.0552` n `7`; unknown avg `-0.1906` n `314`
- 1h: commodity avg `-0.0862` n `7`; crypto_alt avg `0.6435` n `223`; crypto_major avg `0.9124` n `7`; equity avg `-0.0786` n `42`; fx avg `0.0013` n `4`; index avg `0.0767` n `9`; metal avg `-0.0499` n `7`; unknown avg `-0.225` n `314`
- 4h: commodity avg `0.0632` n `7`; crypto_alt avg `2.7299` n `223`; crypto_major avg `3.1767` n `7`; equity avg `0.9935` n `42`; fx avg `-0.0316` n `4`; index avg `0.682` n `9`; metal avg `0.1758` n `7`; unknown avg `0.2419` n `314`
- 24h: commodity avg `0.0467` n `7`; crypto_alt avg `2.9165` n `223`; crypto_major avg `3.4005` n `7`; equity avg `1.1473` n `42`; fx avg `-0.0509` n `4`; index avg `0.8179` n `9`; metal avg `0.2981` n `7`; unknown avg `0.5628` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4005`, n `226`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.39`, n `226`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3662`, n `230`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3507`, n `230`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2028`, n `230`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2015`, n `226`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1941`, n `226`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1797`, n `230`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1747`, n `230`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1698`, n `226`, weak_sample_signal
