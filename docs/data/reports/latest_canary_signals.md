# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T21:52:24.666982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0348` n `12`; crypto_alt avg `0.0572` n `230`; crypto_major avg `0.038` n `8`; equity avg `-0.1704` n `98`; fx avg `-0.006` n `6`; index avg `-0.0262` n `25`; metal avg `-0.0185` n `20`; unknown avg `0.0519` n `773`
- 1h: commodity avg `0.1391` n `12`; crypto_alt avg `0.1453` n `230`; crypto_major avg `0.1749` n `8`; equity avg `0.0349` n `98`; fx avg `-0.0176` n `6`; index avg `-0.0124` n `25`; metal avg `-0.0068` n `20`; unknown avg `0.1666` n `773`
- 4h: commodity avg `0.107` n `12`; crypto_alt avg `-0.1216` n `230`; crypto_major avg `-0.1916` n `8`; equity avg `-0.0303` n `98`; fx avg `-0.014` n `6`; index avg `-0.0522` n `25`; metal avg `-0.068` n `20`; unknown avg `0.1623` n `773`
- 24h: commodity avg `0.6157` n `12`; crypto_alt avg `-0.3378` n `230`; crypto_major avg `-0.5027` n `8`; equity avg `-1.0885` n `98`; fx avg `-0.0486` n `6`; index avg `-0.1767` n `25`; metal avg `0.2559` n `20`; unknown avg `1.615` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0869`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
