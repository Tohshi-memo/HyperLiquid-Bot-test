# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T03:15:34.713456+00:00`
- Correlation status: `ready`
- Asset price records: `132`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0398` n `7`; crypto_alt avg `-0.2026` n `223`; crypto_major avg `-0.0572` n `7`; equity avg `0.0002` n `42`; fx avg `0.0021` n `4`; index avg `-0.0014` n `9`; metal avg `0.0145` n `7`; unknown avg `-0.0355` n `313`
- 1h: commodity avg `0.0302` n `7`; crypto_alt avg `-0.2586` n `223`; crypto_major avg `-0.1254` n `7`; equity avg `-0.0063` n `42`; fx avg `0.0013` n `4`; index avg `-0.0162` n `9`; metal avg `0.0139` n `7`; unknown avg `-0.0394` n `313`
- 4h: commodity avg `0.0215` n `7`; crypto_alt avg `-1.363` n `223`; crypto_major avg `-0.7861` n `7`; equity avg `-0.0845` n `42`; fx avg `0.0027` n `4`; index avg `-0.0232` n `9`; metal avg `0.0195` n `7`; unknown avg `-0.0219` n `313`
- 24h: commodity avg `-0.125` n `7`; crypto_alt avg `0.5998` n `223`; crypto_major avg `-0.2636` n `7`; equity avg `0.6632` n `42`; fx avg `0.0107` n `4`; index avg `0.0004` n `9`; metal avg `0.0465` n `7`; unknown avg `0.1083` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4499`, n `128`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.4422`, n `128`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4347`, n `128`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.4329`, n `128`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.4322`, n `128`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4132`, n `124`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4107`, n `124`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4042`, n `124`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.404`, n `128`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3991`, n `124`, moderate_sample_signal
