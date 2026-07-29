# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T22:22:26.402083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0309` n `12`; crypto_alt avg `0.1257` n `230`; crypto_major avg `0.1292` n `8`; equity avg `0.4813` n `102`; fx avg `0.0059` n `6`; index avg `0.0639` n `25`; metal avg `0.0449` n `20`; unknown avg `0.2157` n `778`
- 1h: commodity avg `-0.1187` n `12`; crypto_alt avg `0.9042` n `230`; crypto_major avg `0.8232` n `8`; equity avg `0.9831` n `102`; fx avg `0.0236` n `6`; index avg `0.161` n `25`; metal avg `0.1278` n `20`; unknown avg `0.7887` n `778`
- 4h: commodity avg `-0.0849` n `12`; crypto_alt avg `-0.6961` n `230`; crypto_major avg `-0.5151` n `8`; equity avg `-1.8138` n `102`; fx avg `0.083` n `6`; index avg `-0.3611` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.4912` n `778`
- 24h: commodity avg `0.7511` n `12`; crypto_alt avg `-2.3575` n `230`; crypto_major avg `-0.5874` n `8`; equity avg `-3.666` n `102`; fx avg `0.04` n `6`; index avg `-0.615` n `25`; metal avg `0.324` n `20`; unknown avg `-0.6773` n `760`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
