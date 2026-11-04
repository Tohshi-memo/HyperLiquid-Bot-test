# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T13:52:29.836359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0161` n `13`; crypto_alt avg `-0.0454` n `239`; crypto_major avg `-0.0235` n `8`; equity avg `-0.2551` n `158`; fx avg `0.0053` n `6`; index avg `0.0118` n `27`; metal avg `0.0319` n `20`; unknown avg `19.1805` n `1264`
- 1h: commodity avg `-0.3209` n `13`; crypto_alt avg `-0.0894` n `239`; crypto_major avg `0.0875` n `8`; equity avg `0.1835` n `158`; fx avg `0.0087` n `6`; index avg `0.0387` n `27`; metal avg `-0.0483` n `20`; unknown avg `0.3583` n `1258`
- 4h: commodity avg `-0.4561` n `13`; crypto_alt avg `-0.5898` n `239`; crypto_major avg `-0.5258` n `8`; equity avg `-1.4948` n `158`; fx avg `0.0018` n `6`; index avg `-0.0352` n `27`; metal avg `-0.0463` n `20`; unknown avg `1.6346` n `1250`
- 24h: commodity avg `-0.0639` n `13`; crypto_alt avg `0.5349` n `239`; crypto_major avg `0.0702` n `8`; equity avg `-0.1192` n `158`; fx avg `0.2032` n `6`; index avg `0.0187` n `27`; metal avg `0.5354` n `20`; unknown avg `183.6423` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2527`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
