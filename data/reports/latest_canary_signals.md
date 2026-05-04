# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T02:45:21.453919+00:00`
- Correlation status: `ready`
- Asset price records: `226`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5265` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0739` n `7`; crypto_alt avg `0.2373` n `223`; crypto_major avg `0.4034` n `7`; equity avg `0.2355` n `42`; fx avg `0.0045` n `4`; index avg `0.126` n `9`; metal avg `0.2642` n `7`; unknown avg `0.0511` n `314`
- 1h: commodity avg `0.013` n `7`; crypto_alt avg `1.3543` n `223`; crypto_major avg `1.5757` n `7`; equity avg `0.5803` n `42`; fx avg `0.0218` n `4`; index avg `0.2606` n `9`; metal avg `0.2723` n `7`; unknown avg `-0.1165` n `314`
- 4h: commodity avg `0.4108` n `7`; crypto_alt avg `1.0266` n `223`; crypto_major avg `1.2241` n `7`; equity avg `0.7552` n `42`; fx avg `0.0358` n `4`; index avg `0.5914` n `9`; metal avg `-0.3024` n `7`; unknown avg `-0.0809` n `314`
- 24h: commodity avg `0.0928` n `7`; crypto_alt avg `2.4442` n `223`; crypto_major avg `2.7766` n `7`; equity avg `1.1885` n `42`; fx avg `0.0167` n `4`; index avg `0.6756` n `9`; metal avg `0.2559` n `7`; unknown avg `0.4535` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.373`, n `222`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3723`, n `218`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3656`, n `218`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3574`, n `222`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.195`, n `218`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1943`, n `222`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1941`, n `218`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `222`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1883`, n `222`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1448`, n `222`, weak_sample_signal
