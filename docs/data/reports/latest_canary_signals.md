# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T23:37:29.084539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `13`; crypto_alt avg `0.0522` n `235`; crypto_major avg `-0.0409` n `8`; equity avg `-0.018` n `150`; fx avg `-0.0007` n `6`; index avg `0.0` n `26`; metal avg `-0.008` n `20`; unknown avg `0.0525` n `1116`
- 1h: commodity avg `0.0299` n `13`; crypto_alt avg `0.3417` n `235`; crypto_major avg `-0.0333` n `8`; equity avg `-0.0137` n `150`; fx avg `0.0006` n `6`; index avg `0.0016` n `26`; metal avg `0.0002` n `20`; unknown avg `0.087` n `1114`
- 4h: commodity avg `-0.0296` n `13`; crypto_alt avg `1.4468` n `235`; crypto_major avg `0.4278` n `8`; equity avg `0.1073` n `150`; fx avg `0.0031` n `6`; index avg `0.011` n `26`; metal avg `-0.0235` n `20`; unknown avg `0.4886` n `1026`
- 24h: commodity avg `-0.1338` n `13`; crypto_alt avg `2.165` n `235`; crypto_major avg `0.3281` n `8`; equity avg `0.8943` n `150`; fx avg `-0.0063` n `6`; index avg `0.1387` n `26`; metal avg `0.4906` n `20`; unknown avg `12.9823` n `901`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
