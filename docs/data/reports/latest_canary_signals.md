# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T23:07:27.566930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0367` n `13`; crypto_alt avg `-0.5175` n `239`; crypto_major avg `-0.2583` n `8`; equity avg `-0.2953` n `158`; fx avg `-0.007` n `6`; index avg `-0.0404` n `27`; metal avg `0.0007` n `20`; unknown avg `0.5634` n `1222`
- 1h: commodity avg `-0.0087` n `13`; crypto_alt avg `-0.6379` n `239`; crypto_major avg `-0.5039` n `8`; equity avg `-0.4433` n `158`; fx avg `-0.0219` n `6`; index avg `-0.0228` n `27`; metal avg `0.0015` n `20`; unknown avg `0.1698` n `1222`
- 4h: commodity avg `0.2699` n `13`; crypto_alt avg `-0.7792` n `239`; crypto_major avg `-0.6754` n `8`; equity avg `-0.7149` n `158`; fx avg `-0.0212` n `6`; index avg `-0.2371` n `27`; metal avg `-0.1894` n `20`; unknown avg `1.6818` n `1162`
- 24h: commodity avg `0.9467` n `13`; crypto_alt avg `-6.0361` n `239`; crypto_major avg `-6.2386` n `8`; equity avg `-8.8502` n `158`; fx avg `0.0513` n `6`; index avg `-1.3533` n `27`; metal avg `0.0218` n `20`; unknown avg `233.6333` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
