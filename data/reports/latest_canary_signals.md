# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T08:37:30.033808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0217` n `13`; crypto_alt avg `-0.1185` n `237`; crypto_major avg `-0.0928` n `8`; equity avg `-0.0961` n `152`; fx avg `-0.0289` n `6`; index avg `-0.025` n `26`; metal avg `-0.0343` n `20`; unknown avg `0.6005` n `1233`
- 1h: commodity avg `0.0091` n `13`; crypto_alt avg `-0.1869` n `237`; crypto_major avg `-0.0173` n `8`; equity avg `0.3331` n `152`; fx avg `-0.0199` n `6`; index avg `0.0326` n `26`; metal avg `-0.042` n `20`; unknown avg `0.0801` n `1165`
- 4h: commodity avg `0.0401` n `13`; crypto_alt avg `0.4295` n `237`; crypto_major avg `0.4632` n `8`; equity avg `1.4782` n `152`; fx avg `-0.0304` n `6`; index avg `0.0933` n `26`; metal avg `0.0539` n `20`; unknown avg `0.1362` n `1148`
- 24h: commodity avg `0.104` n `13`; crypto_alt avg `0.4475` n `237`; crypto_major avg `0.6061` n `8`; equity avg `-0.4218` n `152`; fx avg `-0.0845` n `6`; index avg `-0.034` n `26`; metal avg `-0.4404` n `20`; unknown avg `55.2429` n `858`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
