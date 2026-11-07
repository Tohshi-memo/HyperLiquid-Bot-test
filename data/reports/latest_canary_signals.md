# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T11:52:30.481979+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `0.0845` n `239`; crypto_major avg `0.0144` n `8`; equity avg `-0.0258` n `158`; fx avg `0.0072` n `6`; index avg `-0.0055` n `27`; metal avg `0.0021` n `20`; unknown avg `1.0704` n `1261`
- 1h: commodity avg `0.0272` n `13`; crypto_alt avg `0.0894` n `239`; crypto_major avg `0.0834` n `8`; equity avg `0.0017` n `158`; fx avg `0.017` n `6`; index avg `-0.0088` n `27`; metal avg `-0.0031` n `20`; unknown avg `0.9447` n `1255`
- 4h: commodity avg `0.0619` n `13`; crypto_alt avg `-0.6861` n `239`; crypto_major avg `-0.2366` n `8`; equity avg `0.0493` n `158`; fx avg `0.0032` n `6`; index avg `-0.0058` n `27`; metal avg `-0.0015` n `20`; unknown avg `137.0477` n `1199`
- 24h: commodity avg `-0.0368` n `13`; crypto_alt avg `-1.404` n `239`; crypto_major avg `-0.642` n `8`; equity avg `-0.8743` n `158`; fx avg `-0.0182` n `6`; index avg `-0.0466` n `27`; metal avg `-0.0034` n `20`; unknown avg `8.2635` n `1099`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
