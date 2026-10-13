# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T06:07:32.045649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `13`; crypto_alt avg `-0.2951` n `235`; crypto_major avg `-0.132` n `8`; equity avg `-0.1655` n `151`; fx avg `0.0077` n `6`; index avg `-0.0178` n `26`; metal avg `0.0138` n `20`; unknown avg `0.2756` n `1117`
- 1h: commodity avg `0.0385` n `13`; crypto_alt avg `-0.097` n `235`; crypto_major avg `0.0681` n `8`; equity avg `0.0154` n `151`; fx avg `0.0275` n `6`; index avg `0.0044` n `26`; metal avg `-0.0102` n `20`; unknown avg `0.9232` n `1117`
- 4h: commodity avg `-0.0967` n `13`; crypto_alt avg `2.0794` n `235`; crypto_major avg `1.5082` n `8`; equity avg `0.3952` n `151`; fx avg `0.0899` n `6`; index avg `0.0404` n `26`; metal avg `0.2015` n `20`; unknown avg `1.6763` n `1075`
- 24h: commodity avg `0.4545` n `13`; crypto_alt avg `-3.8967` n `235`; crypto_major avg `-2.208` n `8`; equity avg `-3.5743` n `151`; fx avg `0.0291` n `6`; index avg `-0.5002` n `26`; metal avg `-0.0153` n `20`; unknown avg `0.4273` n `855`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1968`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1822`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1392`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1178`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1067`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0852`, n `666`, weak_sample_signal
