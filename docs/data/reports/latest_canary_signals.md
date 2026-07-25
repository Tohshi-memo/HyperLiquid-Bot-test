# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T04:52:34.028556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `12`; crypto_alt avg `0.0474` n `230`; crypto_major avg `0.0202` n `8`; equity avg `0.0177` n `100`; fx avg `0.0056` n `6`; index avg `0.0036` n `25`; metal avg `0.0036` n `20`; unknown avg `-0.3091` n `774`
- 1h: commodity avg `0.0028` n `12`; crypto_alt avg `0.1706` n `230`; crypto_major avg `0.094` n `8`; equity avg `0.0574` n `100`; fx avg `-0.0022` n `6`; index avg `0.0181` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.292` n `774`
- 4h: commodity avg `-0.2004` n `12`; crypto_alt avg `0.0997` n `230`; crypto_major avg `0.1383` n `8`; equity avg `0.2755` n `100`; fx avg `-0.0252` n `6`; index avg `0.0516` n `25`; metal avg `-0.0242` n `20`; unknown avg `-0.2322` n `774`
- 24h: commodity avg `-0.4481` n `12`; crypto_alt avg `-1.0377` n `230`; crypto_major avg `-0.8386` n `8`; equity avg `-2.1781` n `100`; fx avg `-0.0715` n `6`; index avg `-0.1112` n `25`; metal avg `0.1997` n `20`; unknown avg `13.8628` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1145`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1055`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
