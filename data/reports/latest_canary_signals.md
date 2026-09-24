# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T21:52:31.861975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.082` n `234`; crypto_major avg `-0.0096` n `8`; equity avg `0.025` n `141`; fx avg `0.0002` n `6`; index avg `0.0041` n `26`; metal avg `0.0014` n `20`; unknown avg `0.698` n `946`
- 1h: commodity avg `-0.0293` n `12`; crypto_alt avg `0.3291` n `234`; crypto_major avg `0.0835` n `8`; equity avg `0.0675` n `141`; fx avg `-0.0162` n `6`; index avg `0.005` n `26`; metal avg `-0.0187` n `20`; unknown avg `2.2302` n `942`
- 4h: commodity avg `-0.312` n `12`; crypto_alt avg `0.6599` n `234`; crypto_major avg `0.398` n `8`; equity avg `0.0972` n `141`; fx avg `-0.0206` n `6`; index avg `0.0087` n `26`; metal avg `0.049` n `20`; unknown avg `8.214` n `869`
- 24h: commodity avg `0.731` n `12`; crypto_alt avg `4.2454` n `234`; crypto_major avg `1.3933` n `8`; equity avg `-0.2524` n `141`; fx avg `0.0258` n `6`; index avg `-0.1089` n `26`; metal avg `-0.1561` n `20`; unknown avg `19.5404` n `855`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
