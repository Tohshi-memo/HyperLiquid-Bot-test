# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T22:00:28.109284+00:00`
- Correlation status: `ready`
- Asset price records: `111`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `7`; crypto_alt avg `-0.1363` n `223`; crypto_major avg `-0.076` n `7`; equity avg `0.0393` n `42`; fx avg `0.0101` n `4`; index avg `-0.0058` n `9`; metal avg `0.0025` n `7`; unknown avg `-0.047` n `313`
- 1h: commodity avg `-0.0269` n `7`; crypto_alt avg `0.2277` n `223`; crypto_major avg `0.2031` n `7`; equity avg `0.0314` n `42`; fx avg `0.0276` n `4`; index avg `-0.0156` n `9`; metal avg `0.0085` n `7`; unknown avg `0.0406` n `313`
- 4h: commodity avg `-0.0379` n `7`; crypto_alt avg `0.6813` n `223`; crypto_major avg `0.3635` n `7`; equity avg `0.4085` n `42`; fx avg `0.0473` n `4`; index avg `0.0338` n `9`; metal avg `-0.0053` n `7`; unknown avg `0.1926` n `313`
- 24h: commodity avg `-0.166` n `7`; crypto_alt avg `2.0291` n `223`; crypto_major avg `0.6815` n `7`; equity avg `0.9635` n `42`; fx avg `0.0468` n `4`; index avg `0.009` n `9`; metal avg `0.0209` n `7`; unknown avg `0.3447` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.538`, n `103`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5265`, n `103`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4922`, n `107`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.475`, n `107`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4641`, n `103`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4208`, n `103`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.419`, n `103`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4173`, n `103`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4172`, n `103`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4084`, n `107`, moderate_sample_signal
