# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T04:15:31.145642+00:00`
- Correlation status: `ready`
- Asset price records: `232`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7642` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6516` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.612` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0638` n `7`; crypto_alt avg `0.0835` n `223`; crypto_major avg `0.227` n `7`; equity avg `-0.1082` n `42`; fx avg `-0.0242` n `4`; index avg `0.0031` n `9`; metal avg `0.0606` n `7`; unknown avg `-0.2082` n `314`
- 1h: commodity avg `-0.0536` n `7`; crypto_alt avg `0.2925` n `223`; crypto_major avg `0.272` n `7`; equity avg `-0.1278` n `42`; fx avg `-0.0996` n `4`; index avg `-0.0244` n `9`; metal avg `-0.0266` n `7`; unknown avg `-0.1789` n `314`
- 4h: commodity avg `-0.0791` n `7`; crypto_alt avg `2.5599` n `223`; crypto_major avg `2.6851` n `7`; equity avg `1.0731` n `42`; fx avg `-0.0464` n `4`; index avg `0.6786` n `9`; metal avg `0.0335` n `7`; unknown avg `0.1966` n `314`
- 24h: commodity avg `0.0115` n `7`; crypto_alt avg `3.0557` n `223`; crypto_major avg `3.1597` n `7`; equity avg `1.1808` n `42`; fx avg `-0.0734` n `4`; index avg `0.8319` n `9`; metal avg `0.371` n `7`; unknown avg `0.5866` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3947`, n `224`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3842`, n `224`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3661`, n `228`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3505`, n `228`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2102`, n `224`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1972`, n `224`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1961`, n `228`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1874`, n `228`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1818`, n `228`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1603`, n `224`, weak_sample_signal
