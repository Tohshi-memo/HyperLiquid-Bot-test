# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T20:52:36.875748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `13`; crypto_alt avg `-0.0282` n `239`; crypto_major avg `0.0372` n `8`; equity avg `0.0122` n `168`; fx avg `-0.0011` n `6`; index avg `-0.0028` n `27`; metal avg `0.0004` n `20`; unknown avg `2.9163` n `1264`
- 1h: commodity avg `0.0273` n `13`; crypto_alt avg `-0.1072` n `239`; crypto_major avg `-0.033` n `8`; equity avg `0.0219` n `168`; fx avg `-0.002` n `6`; index avg `-0.0022` n `27`; metal avg `-0.0011` n `20`; unknown avg `1.7765` n `1222`
- 4h: commodity avg `0.1207` n `13`; crypto_alt avg `-0.2344` n `239`; crypto_major avg `-0.189` n `8`; equity avg `0.1506` n `168`; fx avg `-0.0121` n `6`; index avg `0.0112` n `27`; metal avg `0.0111` n `20`; unknown avg `54.258` n `1193`
- 24h: commodity avg `-0.0158` n `13`; crypto_alt avg `-3.3836` n `239`; crypto_major avg `-1.3479` n `8`; equity avg `-0.1054` n `168`; fx avg `-0.0071` n `6`; index avg `-0.0573` n `27`; metal avg `0.037` n `20`; unknown avg `0.902` n `1047`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
