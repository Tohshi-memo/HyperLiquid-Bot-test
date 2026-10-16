# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T06:37:29.475817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0116` n `13`; crypto_alt avg `0.2092` n `236`; crypto_major avg `0.1333` n `8`; equity avg `-0.005` n `151`; fx avg `-0.0266` n `6`; index avg `0.02` n `26`; metal avg `0.0319` n `20`; unknown avg `0.2035` n `1136`
- 1h: commodity avg `-0.0059` n `13`; crypto_alt avg `0.3134` n `236`; crypto_major avg `0.1986` n `8`; equity avg `-0.3538` n `151`; fx avg `-0.0535` n `6`; index avg `-0.069` n `26`; metal avg `-0.0246` n `20`; unknown avg `-0.115` n `1110`
- 4h: commodity avg `0.0453` n `13`; crypto_alt avg `0.5694` n `236`; crypto_major avg `0.2577` n `8`; equity avg `-0.1387` n `151`; fx avg `-0.0802` n `6`; index avg `-0.0387` n `26`; metal avg `0.034` n `20`; unknown avg `0.6876` n `1102`
- 24h: commodity avg `-0.0602` n `13`; crypto_alt avg `4.393` n `236`; crypto_major avg `2.1964` n `8`; equity avg `2.1768` n `151`; fx avg `0.004` n `6`; index avg `0.3306` n `26`; metal avg `0.4956` n `20`; unknown avg `26.3293` n `904`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0993`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0984`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0942`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0903`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0767`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0649`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
