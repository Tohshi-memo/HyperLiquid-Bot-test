# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T18:37:26.924696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `-0.0132` n `234`; crypto_major avg `0.036` n `8`; equity avg `0.008` n `141`; fx avg `0.0009` n `6`; index avg `-0.0005` n `26`; metal avg `0.0019` n `20`; unknown avg `1.2915` n `962`
- 1h: commodity avg `0.017` n `12`; crypto_alt avg `0.5267` n `234`; crypto_major avg `0.4775` n `8`; equity avg `0.0565` n `141`; fx avg `-0.0012` n `6`; index avg `0.0067` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.0916` n `960`
- 4h: commodity avg `-0.1062` n `12`; crypto_alt avg `0.81` n `234`; crypto_major avg `0.3948` n `8`; equity avg `0.1858` n `141`; fx avg `0.0075` n `6`; index avg `0.0378` n `26`; metal avg `0.0068` n `20`; unknown avg `7.1461` n `954`
- 24h: commodity avg `-0.1309` n `12`; crypto_alt avg `0.4705` n `234`; crypto_major avg `0.5749` n `8`; equity avg `0.3813` n `141`; fx avg `-0.0179` n `6`; index avg `0.0401` n `26`; metal avg `-0.0056` n `20`; unknown avg `120.1113` n `897`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
