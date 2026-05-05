# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T11:15:30.388993+00:00`
- Correlation status: `ready`
- Asset price records: `355`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1397` n `7`; crypto_alt avg `-0.1897` n `223`; crypto_major avg `-0.0032` n `7`; equity avg `0.1108` n `47`; fx avg `0.0044` n `4`; index avg `-0.0694` n `6`; metal avg `0.1777` n `7`; unknown avg `-0.2342` n `312`
- 1h: commodity avg `0.2706` n `7`; crypto_alt avg `0.0042` n `223`; crypto_major avg `0.4436` n `7`; equity avg `0.299` n `47`; fx avg `0.0126` n `4`; index avg `-0.0795` n `6`; metal avg `-0.116` n `7`; unknown avg `0.1392` n `312`
- 4h: commodity avg `0.1948` n `7`; crypto_alt avg `0.2751` n `223`; crypto_major avg `0.1456` n `7`; equity avg `-0.0506` n `47`; fx avg `0.0736` n `4`; index avg `-0.1347` n `6`; metal avg `0.0703` n `7`; unknown avg `0.2012` n `312`
- 24h: commodity avg `0.4352` n `7`; crypto_alt avg `2.0774` n `223`; crypto_major avg `1.9386` n `7`; equity avg `0.6141` n `47`; fx avg `0.0603` n `4`; index avg `0.2701` n `6`; metal avg `0.4338` n `7`; unknown avg `-0.6367` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2169`, n `351`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2099`, n `351`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1373`, n `351`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1329`, n `351`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1238`, n `351`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1142`, n `351`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1058`, n `351`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `351`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.105`, n `347`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0945`, n `347`, weak_sample_signal
