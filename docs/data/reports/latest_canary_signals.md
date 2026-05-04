# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T05:30:24.222342+00:00`
- Correlation status: `ready`
- Asset price records: `237`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.088` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7789` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0949` n `7`; crypto_alt avg `-0.1123` n `223`; crypto_major avg `-0.1783` n `7`; equity avg `-0.1034` n `42`; fx avg `0.0114` n `4`; index avg `0.0991` n `9`; metal avg `-0.1328` n `7`; unknown avg `-0.3927` n `314`
- 1h: commodity avg `-0.1346` n `7`; crypto_alt avg `-0.3946` n `223`; crypto_major avg `-0.4394` n `7`; equity avg `-0.1286` n `42`; fx avg `0.0165` n `4`; index avg `0.0858` n `9`; metal avg `-0.3172` n `7`; unknown avg `-0.4321` n `314`
- 4h: commodity avg `-0.139` n `7`; crypto_alt avg `1.7192` n `223`; crypto_major avg `1.949` n `7`; equity avg `0.5731` n `42`; fx avg `-0.022` n `4`; index avg `0.5885` n `9`; metal avg `0.1701` n `7`; unknown avg `-0.2481` n `314`
- 24h: commodity avg `-0.0937` n `7`; crypto_alt avg `2.4571` n `223`; crypto_major avg `2.7528` n `7`; equity avg `1.0641` n `42`; fx avg `-0.039` n `4`; index avg `0.9611` n `9`; metal avg `0.021` n `7`; unknown avg `0.1333` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3949`, n `229`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.385`, n `229`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3632`, n `233`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3483`, n `233`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1955`, n `233`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1871`, n `229`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1837`, n `229`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.179`, n `233`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1739`, n `233`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1511`, n `229`, weak_sample_signal
