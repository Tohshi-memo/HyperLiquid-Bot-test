# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T00:22:27.700722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0323` n `13`; crypto_alt avg `-0.0926` n `239`; crypto_major avg `0.0198` n `8`; equity avg `-0.0532` n `158`; fx avg `0.0072` n `6`; index avg `-0.0058` n `27`; metal avg `-0.0025` n `20`; unknown avg `0.3278` n `1262`
- 1h: commodity avg `-0.0928` n `13`; crypto_alt avg `0.0429` n `239`; crypto_major avg `0.2236` n `8`; equity avg `0.0525` n `158`; fx avg `0.0151` n `6`; index avg `0.0119` n `27`; metal avg `0.0054` n `20`; unknown avg `0.1956` n `1250`
- 4h: commodity avg `-0.0637` n `13`; crypto_alt avg `-0.1092` n `239`; crypto_major avg `0.1752` n `8`; equity avg `-0.016` n `158`; fx avg `0.0074` n `6`; index avg `0.0021` n `27`; metal avg `0.0011` n `20`; unknown avg `0.3461` n `1200`
- 24h: commodity avg `-0.0227` n `13`; crypto_alt avg `-1.331` n `239`; crypto_major avg `-0.6025` n `8`; equity avg `-0.0252` n `158`; fx avg `0.004` n `6`; index avg `0.0669` n `27`; metal avg `-0.0256` n `20`; unknown avg `160.5884` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
