# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T00:37:26.984706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0357` n `12`; crypto_alt avg `-0.2163` n `230`; crypto_major avg `-0.1061` n `8`; equity avg `-0.2043` n `100`; fx avg `-0.0153` n `6`; index avg `-0.0599` n `25`; metal avg `0.0333` n `20`; unknown avg `0.0605` n `772`
- 1h: commodity avg `-0.0016` n `12`; crypto_alt avg `-0.4002` n `230`; crypto_major avg `-0.3902` n `8`; equity avg `-0.4142` n `100`; fx avg `-0.0293` n `6`; index avg `-0.1486` n `25`; metal avg `0.0124` n `20`; unknown avg `0.0479` n `772`
- 4h: commodity avg `0.0699` n `12`; crypto_alt avg `-0.8502` n `230`; crypto_major avg `-0.6166` n `8`; equity avg `-0.8743` n `100`; fx avg `-0.0496` n `6`; index avg `-0.2092` n `25`; metal avg `-0.0129` n `20`; unknown avg `-0.2202` n `772`
- 24h: commodity avg `0.6268` n `12`; crypto_alt avg `-2.2219` n `230`; crypto_major avg `-2.7459` n `8`; equity avg `-2.1362` n `99`; fx avg `-0.0783` n `6`; index avg `-0.512` n `25`; metal avg `-0.7708` n `20`; unknown avg `-0.3159` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0807`, n `666`, weak_sample_signal
