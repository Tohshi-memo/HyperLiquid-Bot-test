# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T08:37:30.303101+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0319` n `13`; crypto_alt avg `0.3372` n `239`; crypto_major avg `0.272` n `8`; equity avg `0.1032` n `158`; fx avg `0.007` n `6`; index avg `0.0303` n `27`; metal avg `0.0048` n `20`; unknown avg `-0.1059` n `1265`
- 1h: commodity avg `-0.0139` n `13`; crypto_alt avg `0.7155` n `239`; crypto_major avg `0.628` n `8`; equity avg `0.2944` n `158`; fx avg `0.0087` n `6`; index avg `0.0739` n `27`; metal avg `0.0467` n `20`; unknown avg `0.3118` n `1243`
- 4h: commodity avg `0.3022` n `13`; crypto_alt avg `0.0687` n `239`; crypto_major avg `0.2438` n `8`; equity avg `0.1347` n `158`; fx avg `-0.0427` n `6`; index avg `0.0467` n `27`; metal avg `-0.1311` n `20`; unknown avg `0.0088` n `1211`
- 24h: commodity avg `-1.7891` n `13`; crypto_alt avg `0.7866` n `239`; crypto_major avg `2.0473` n `8`; equity avg `-2.468` n `158`; fx avg `0.0211` n `6`; index avg `-0.109` n `27`; metal avg `0.7019` n `20`; unknown avg `29.8448` n `1038`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.249`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1821`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
