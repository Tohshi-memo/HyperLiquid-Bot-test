# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T01:22:29.264623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0533` n `13`; crypto_alt avg `-0.1002` n `238`; crypto_major avg `-0.0447` n `8`; equity avg `-0.386` n `155`; fx avg `0.007` n `6`; index avg `-0.0876` n `27`; metal avg `0.0769` n `20`; unknown avg `-0.259` n `1236`
- 1h: commodity avg `-0.0093` n `13`; crypto_alt avg `-0.547` n `238`; crypto_major avg `-0.4411` n `8`; equity avg `-0.4713` n `155`; fx avg `-0.0426` n `6`; index avg `-0.0958` n `27`; metal avg `0.1335` n `20`; unknown avg `0.1832` n `1232`
- 4h: commodity avg `0.0433` n `13`; crypto_alt avg `-1.2365` n `238`; crypto_major avg `-0.9071` n `8`; equity avg `-0.2949` n `155`; fx avg `-0.1097` n `6`; index avg `-0.0488` n `27`; metal avg `0.0208` n `20`; unknown avg `1.9392` n `1150`
- 24h: commodity avg `0.0195` n `13`; crypto_alt avg `-0.2474` n `238`; crypto_major avg `-0.1759` n `8`; equity avg `-0.0733` n `154`; fx avg `0.0635` n `6`; index avg `-0.0223` n `27`; metal avg `-0.0821` n `20`; unknown avg `25.7194` n `996`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
