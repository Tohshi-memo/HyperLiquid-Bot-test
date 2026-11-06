# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T23:07:32.395570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0267` n `13`; crypto_alt avg `-0.2081` n `239`; crypto_major avg `-0.1446` n `8`; equity avg `-0.0522` n `158`; fx avg `-0.0012` n `6`; index avg `-0.0125` n `27`; metal avg `0.0136` n `20`; unknown avg `0.1162` n `1241`
- 1h: commodity avg `0.0176` n `13`; crypto_alt avg `-0.4906` n `239`; crypto_major avg `-0.3128` n `8`; equity avg `-0.157` n `158`; fx avg `0.009` n `6`; index avg `-0.0231` n `27`; metal avg `0.0089` n `20`; unknown avg `0.2359` n `1239`
- 4h: commodity avg `0.1038` n `13`; crypto_alt avg `-0.5671` n `239`; crypto_major avg `-0.1591` n `8`; equity avg `0.2197` n `158`; fx avg `0.0131` n `6`; index avg `-0.0398` n `27`; metal avg `-0.0324` n `20`; unknown avg `0.1527` n `1165`
- 24h: commodity avg `0.0439` n `13`; crypto_alt avg `2.0795` n `239`; crypto_major avg `0.438` n `8`; equity avg `3.3504` n `158`; fx avg `-0.0612` n `6`; index avg `0.4432` n `27`; metal avg `0.0642` n `20`; unknown avg `8.8766` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
