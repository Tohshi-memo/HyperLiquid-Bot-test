# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T10:37:28.714991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `13`; crypto_alt avg `-0.2315` n `239`; crypto_major avg `-0.1568` n `8`; equity avg `0.0035` n `158`; fx avg `0.0094` n `6`; index avg `0.0004` n `27`; metal avg `-0.0007` n `20`; unknown avg `0.147` n `1261`
- 1h: commodity avg `0.0417` n `13`; crypto_alt avg `-0.4554` n `239`; crypto_major avg `-0.2085` n `8`; equity avg `-0.1135` n `158`; fx avg `0.0111` n `6`; index avg `-0.0232` n `27`; metal avg `0.0125` n `20`; unknown avg `1.8259` n `1255`
- 4h: commodity avg `0.0974` n `13`; crypto_alt avg `-0.7298` n `239`; crypto_major avg `-0.2902` n `8`; equity avg `0.0709` n `158`; fx avg `-0.003` n `6`; index avg `0.0006` n `27`; metal avg `0.006` n `20`; unknown avg `136.5311` n `1195`
- 24h: commodity avg `-0.029` n `13`; crypto_alt avg `-1.2413` n `239`; crypto_major avg `-0.5909` n `8`; equity avg `-0.2277` n `158`; fx avg `0.037` n `6`; index avg `-0.0292` n `27`; metal avg `0.0841` n `20`; unknown avg `7.8446` n `1047`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
