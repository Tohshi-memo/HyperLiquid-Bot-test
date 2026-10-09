# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T17:37:33.170574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0756` n `13`; crypto_alt avg `0.2263` n `235`; crypto_major avg `0.2193` n `8`; equity avg `0.0622` n `150`; fx avg `-0.0091` n `6`; index avg `0.0056` n `26`; metal avg `-0.0072` n `20`; unknown avg `0.3004` n `1092`
- 1h: commodity avg `-0.0142` n `13`; crypto_alt avg `0.0786` n `235`; crypto_major avg `0.0526` n `8`; equity avg `0.058` n `150`; fx avg `0.0079` n `6`; index avg `-0.0013` n `26`; metal avg `0.0204` n `20`; unknown avg `0.4923` n `1082`
- 4h: commodity avg `0.1411` n `13`; crypto_alt avg `0.6436` n `235`; crypto_major avg `0.199` n `8`; equity avg `0.0707` n `150`; fx avg `0.007` n `6`; index avg `0.0022` n `26`; metal avg `-0.0396` n `20`; unknown avg `-0.2218` n `996`
- 24h: commodity avg `0.1424` n `13`; crypto_alt avg `4.3102` n `235`; crypto_major avg `2.6061` n `8`; equity avg `1.5337` n `150`; fx avg `0.034` n `6`; index avg `0.2328` n `26`; metal avg `0.6028` n `20`; unknown avg `1.9303` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
