# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T22:37:28.154960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0749` n `13`; crypto_alt avg `0.3115` n `235`; crypto_major avg `0.137` n `8`; equity avg `0.0149` n `150`; fx avg `0.0` n `6`; index avg `0.0107` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.1191` n `1116`
- 1h: commodity avg `-0.0524` n `13`; crypto_alt avg `0.2982` n `235`; crypto_major avg `0.1495` n `8`; equity avg `0.0166` n `150`; fx avg `-0.003` n `6`; index avg `-0.0084` n `26`; metal avg `-0.0145` n `20`; unknown avg `-0.0166` n `1114`
- 4h: commodity avg `-0.2627` n `13`; crypto_alt avg `0.4609` n `235`; crypto_major avg `0.118` n `8`; equity avg `0.0002` n `150`; fx avg `-0.0063` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0386` n `20`; unknown avg `0.1916` n `1026`
- 24h: commodity avg `-0.1309` n `13`; crypto_alt avg `1.8932` n `235`; crypto_major avg `0.3871` n `8`; equity avg `0.6821` n `150`; fx avg `0.0086` n `6`; index avg `0.1027` n `26`; metal avg `0.5369` n `20`; unknown avg `12.697` n `901`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
