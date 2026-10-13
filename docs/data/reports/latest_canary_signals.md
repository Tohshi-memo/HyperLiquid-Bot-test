# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T12:52:27.063656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0329` n `13`; crypto_alt avg `0.138` n `235`; crypto_major avg `-0.0417` n `8`; equity avg `-0.0837` n `151`; fx avg `0.0108` n `6`; index avg `-0.0224` n `26`; metal avg `-0.0421` n `20`; unknown avg `46.2159` n `1135`
- 1h: commodity avg `-0.0262` n `13`; crypto_alt avg `0.6669` n `235`; crypto_major avg `0.0999` n `8`; equity avg `-0.412` n `151`; fx avg `0.0246` n `6`; index avg `-0.0295` n `26`; metal avg `-0.103` n `20`; unknown avg `7.6681` n `1127`
- 4h: commodity avg `0.1288` n `13`; crypto_alt avg `-1.1629` n `235`; crypto_major avg `-0.7198` n `8`; equity avg `-0.9534` n `151`; fx avg `0.0592` n `6`; index avg `-0.0867` n `26`; metal avg `-0.1473` n `20`; unknown avg `4.8006` n `1127`
- 24h: commodity avg `-0.0291` n `13`; crypto_alt avg `-3.5964` n `235`; crypto_major avg `-1.8036` n `8`; equity avg `-3.3456` n `151`; fx avg `0.092` n `6`; index avg `-0.3884` n `26`; metal avg `-0.0765` n `20`; unknown avg `2.2261` n `990`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1719`, n `666`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1699`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1495`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1491`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0897`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
