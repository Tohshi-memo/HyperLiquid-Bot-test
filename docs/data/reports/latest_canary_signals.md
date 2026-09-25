# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T00:52:33.050666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `12`; crypto_alt avg `-0.1341` n `234`; crypto_major avg `-0.0473` n `8`; equity avg `-0.0585` n `141`; fx avg `-0.0117` n `6`; index avg `-0.0035` n `26`; metal avg `0.0108` n `20`; unknown avg `0.4926` n `946`
- 1h: commodity avg `-0.0944` n `12`; crypto_alt avg `-0.0172` n `234`; crypto_major avg `0.101` n `8`; equity avg `0.0654` n `141`; fx avg `-0.0301` n `6`; index avg `0.0077` n `26`; metal avg `-0.0354` n `20`; unknown avg `0.3432` n `938`
- 4h: commodity avg `-0.3493` n `12`; crypto_alt avg `-0.0202` n `234`; crypto_major avg `-0.1092` n `8`; equity avg `0.0555` n `141`; fx avg `-0.0269` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0563` n `20`; unknown avg `3.6141` n `896`
- 24h: commodity avg `0.5548` n `12`; crypto_alt avg `3.905` n `234`; crypto_major avg `1.1338` n `8`; equity avg `-0.0226` n `141`; fx avg `-0.0689` n `6`; index avg `-0.0803` n `26`; metal avg `-0.1147` n `20`; unknown avg `23.3206` n `815`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
