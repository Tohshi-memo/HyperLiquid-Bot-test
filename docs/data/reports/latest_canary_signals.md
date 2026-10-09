# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T17:07:31.488170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0771` n `13`; crypto_alt avg `-0.1541` n `235`; crypto_major avg `-0.1223` n `8`; equity avg `-0.0682` n `150`; fx avg `0.0087` n `6`; index avg `-0.0132` n `26`; metal avg `-0.0201` n `20`; unknown avg `0.5644` n `1090`
- 1h: commodity avg `-0.1376` n `13`; crypto_alt avg `-0.1011` n `235`; crypto_major avg `-0.1511` n `8`; equity avg `0.0821` n `150`; fx avg `-0.0073` n `6`; index avg `0.0065` n `26`; metal avg `-0.0535` n `20`; unknown avg `2.2185` n `1082`
- 4h: commodity avg `0.1587` n `13`; crypto_alt avg `0.1603` n `235`; crypto_major avg `-0.494` n `8`; equity avg `-0.46` n `150`; fx avg `0.0006` n `6`; index avg `-0.0548` n `26`; metal avg `0.0694` n `20`; unknown avg `-0.146` n `996`
- 24h: commodity avg `0.1383` n `13`; crypto_alt avg `3.9286` n `235`; crypto_major avg `2.2714` n `8`; equity avg `1.3691` n `150`; fx avg `0.0447` n `6`; index avg `0.2314` n `26`; metal avg `0.5781` n `20`; unknown avg `1.583` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
