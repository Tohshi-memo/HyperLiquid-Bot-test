# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T07:52:25.727439+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `13`; crypto_alt avg `0.0513` n `239`; crypto_major avg `0.1156` n `8`; equity avg `0.028` n `158`; fx avg `0.0046` n `6`; index avg `0.0111` n `27`; metal avg `0.0013` n `20`; unknown avg `-0.0174` n `1261`
- 1h: commodity avg `0.0471` n `13`; crypto_alt avg `0.1062` n `239`; crypto_major avg `0.083` n `8`; equity avg `0.0427` n `158`; fx avg `0.0067` n `6`; index avg `0.0073` n `27`; metal avg `-0.0022` n `20`; unknown avg `11.5554` n `1253`
- 4h: commodity avg `0.0514` n `13`; crypto_alt avg `0.3475` n `239`; crypto_major avg `0.2684` n `8`; equity avg `-0.1273` n `158`; fx avg `-0.0168` n `6`; index avg `0.0015` n `27`; metal avg `-0.0056` n `20`; unknown avg `12.1593` n `1207`
- 24h: commodity avg `-0.2803` n `13`; crypto_alt avg `0.5355` n `239`; crypto_major avg `0.634` n `8`; equity avg `1.1203` n `158`; fx avg `0.0262` n `6`; index avg `0.1941` n `27`; metal avg `0.1881` n `20`; unknown avg `8.3106` n `1008`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
