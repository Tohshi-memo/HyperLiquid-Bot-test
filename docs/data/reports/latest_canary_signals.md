# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T00:52:27.760018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `13`; crypto_alt avg `0.0179` n `235`; crypto_major avg `0.0024` n `8`; equity avg `0.0179` n `150`; fx avg `0.0037` n `6`; index avg `0.003` n `26`; metal avg `0.0062` n `20`; unknown avg `0.0582` n `1116`
- 1h: commodity avg `-0.0183` n `13`; crypto_alt avg `0.3356` n `235`; crypto_major avg `0.1249` n `8`; equity avg `0.0697` n `150`; fx avg `0.0087` n `6`; index avg `0.0306` n `26`; metal avg `0.028` n `20`; unknown avg `0.0723` n `1108`
- 4h: commodity avg `-0.0694` n `13`; crypto_alt avg `1.4528` n `235`; crypto_major avg `0.4951` n `8`; equity avg `0.0714` n `150`; fx avg `0.0029` n `6`; index avg `0.0187` n `26`; metal avg `0.0028` n `20`; unknown avg `0.2993` n `1092`
- 24h: commodity avg `-0.1955` n `13`; crypto_alt avg `3.0067` n `235`; crypto_major avg `0.596` n `8`; equity avg `0.7922` n `150`; fx avg `-0.0521` n `6`; index avg `0.121` n `26`; metal avg `0.4996` n `20`; unknown avg `13.3325` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
