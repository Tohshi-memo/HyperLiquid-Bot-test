# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T05:45:26.224438+00:00`
- Correlation status: `ready`
- Asset price records: `238`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0297` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7439` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0368` n `7`; crypto_alt avg `0.2834` n `223`; crypto_major avg `0.0985` n `7`; equity avg `-0.0175` n `42`; fx avg `0.0013` n `4`; index avg `-0.0179` n `9`; metal avg `0.0472` n `7`; unknown avg `-0.0787` n `314`
- 1h: commodity avg `-0.1922` n `7`; crypto_alt avg `-0.185` n `223`; crypto_major avg `-0.4602` n `7`; equity avg `-0.1715` n `42`; fx avg `0.0168` n `4`; index avg `0.0815` n `9`; metal avg `-0.2152` n `7`; unknown avg `-0.278` n `314`
- 4h: commodity avg `-0.1732` n `7`; crypto_alt avg `1.7786` n `223`; crypto_major avg `1.8565` n `7`; equity avg `0.377` n `42`; fx avg `-0.0313` n `4`; index avg `0.4948` n `9`; metal avg `0.1126` n `7`; unknown avg `-0.1015` n `314`
- 24h: commodity avg `-0.1235` n `7`; crypto_alt avg `2.8485` n `223`; crypto_major avg `2.9046` n `7`; equity avg `0.9979` n `42`; fx avg `-0.0416` n `4`; index avg `0.917` n `9`; metal avg `0.0754` n `7`; unknown avg `0.277` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3987`, n `230`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3888`, n `230`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3623`, n `234`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3477`, n `234`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1932`, n `234`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.188`, n `230`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1834`, n `230`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.179`, n `234`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1738`, n `234`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1441`, n `230`, weak_sample_signal
