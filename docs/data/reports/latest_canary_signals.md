# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T20:22:33.602430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `0.0563` n `230`; crypto_major avg `0.0855` n `8`; equity avg `0.1266` n `100`; fx avg `-0.0053` n `6`; index avg `0.022` n `25`; metal avg `0.0007` n `20`; unknown avg `0.0435` n `774`
- 1h: commodity avg `0.098` n `12`; crypto_alt avg `0.0995` n `230`; crypto_major avg `0.0284` n `8`; equity avg `0.2397` n `100`; fx avg `-0.0096` n `6`; index avg `0.0321` n `25`; metal avg `0.0093` n `20`; unknown avg `0.0496` n `773`
- 4h: commodity avg `0.1675` n `12`; crypto_alt avg `0.0185` n `230`; crypto_major avg `-0.0297` n `8`; equity avg `-1.5041` n `100`; fx avg `-0.0388` n `6`; index avg `-0.2772` n `25`; metal avg `-0.254` n `20`; unknown avg `-0.0396` n `773`
- 24h: commodity avg `-0.3335` n `12`; crypto_alt avg `-1.1707` n `230`; crypto_major avg `-1.0732` n `8`; equity avg `-3.499` n `100`; fx avg `-0.1672` n `6`; index avg `-0.5045` n `25`; metal avg `-0.0244` n `20`; unknown avg `13.8911` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1554`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1297`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1246`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1154`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1121`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1101`, n `666`, weak_sample_signal
