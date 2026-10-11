# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T08:22:29.070666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `13`; crypto_alt avg `0.1063` n `235`; crypto_major avg `0.0486` n `8`; equity avg `0.0072` n `150`; fx avg `-0.001` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0` n `20`; unknown avg `0.0497` n `1117`
- 1h: commodity avg `0.0253` n `13`; crypto_alt avg `-0.0217` n `235`; crypto_major avg `0.0184` n `8`; equity avg `0.0037` n `150`; fx avg `-0.0002` n `6`; index avg `-0.0031` n `26`; metal avg `0.0026` n `20`; unknown avg `0.1438` n `1099`
- 4h: commodity avg `0.0156` n `13`; crypto_alt avg `0.7864` n `235`; crypto_major avg `0.0489` n `8`; equity avg `0.0206` n `150`; fx avg `0.0045` n `6`; index avg `0.003` n `26`; metal avg `0.0119` n `20`; unknown avg `0.4343` n `1083`
- 24h: commodity avg `0.1888` n `13`; crypto_alt avg `1.2083` n `235`; crypto_major avg `-0.1895` n `8`; equity avg `0.0749` n `150`; fx avg `-0.0433` n `6`; index avg `0.0005` n `26`; metal avg `0.006` n `20`; unknown avg `0.4841` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
