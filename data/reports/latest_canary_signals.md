# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T21:37:27.561236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `13`; crypto_alt avg `-0.3541` n `239`; crypto_major avg `-0.2543` n `8`; equity avg `-0.0463` n `158`; fx avg `0.0049` n `6`; index avg `-0.0044` n `27`; metal avg `-0.0092` n `20`; unknown avg `0.5827` n `1231`
- 1h: commodity avg `-0.0175` n `13`; crypto_alt avg `-0.0767` n `239`; crypto_major avg `-0.1726` n `8`; equity avg `-0.0145` n `158`; fx avg `0.0225` n `6`; index avg `-0.0093` n `27`; metal avg `-0.0261` n `20`; unknown avg `0.1737` n `1191`
- 4h: commodity avg `0.1191` n `13`; crypto_alt avg `0.0174` n `239`; crypto_major avg `0.0521` n `8`; equity avg `0.9851` n `158`; fx avg `0.0203` n `6`; index avg `0.0773` n `27`; metal avg `0.0758` n `20`; unknown avg `0.0811` n `1185`
- 24h: commodity avg `0.037` n `13`; crypto_alt avg `1.1639` n `239`; crypto_major avg `-0.6505` n `8`; equity avg `2.2406` n `158`; fx avg `-0.055` n `6`; index avg `0.3925` n `27`; metal avg `-0.0196` n `20`; unknown avg `-0.2267` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
