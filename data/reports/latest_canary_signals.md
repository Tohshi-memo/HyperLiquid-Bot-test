# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T16:07:31.050831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.61` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `-0.0761` n `234`; crypto_major avg `-0.1644` n `8`; equity avg `-0.2042` n `137`; fx avg `0.0054` n `6`; index avg `-0.0258` n `27`; metal avg `-0.0382` n `20`; unknown avg `0.1287` n `915`
- 1h: commodity avg `0.025` n `12`; crypto_alt avg `-0.2548` n `234`; crypto_major avg `-0.1102` n `8`; equity avg `-0.2466` n `137`; fx avg `0.0046` n `6`; index avg `-0.0338` n `27`; metal avg `-0.0673` n `20`; unknown avg `2.5235` n `915`
- 4h: commodity avg `-0.3682` n `12`; crypto_alt avg `-1.3202` n `234`; crypto_major avg `-0.8754` n `8`; equity avg `0.1356` n `137`; fx avg `-0.0018` n `6`; index avg `0.0201` n `27`; metal avg `-0.057` n `20`; unknown avg `8.6525` n `897`
- 24h: commodity avg `-0.5195` n `12`; crypto_alt avg `-2.7683` n `234`; crypto_major avg `-1.8533` n `8`; equity avg `1.0828` n `137`; fx avg `0.0111` n `6`; index avg `0.2821` n `27`; metal avg `0.416` n `20`; unknown avg `5.6023` n `806`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
