# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T23:22:25.244917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.1123` n `230`; crypto_major avg `-0.0799` n `8`; equity avg `0.0081` n `100`; fx avg `0.0261` n `6`; index avg `0.0047` n `25`; metal avg `0.0004` n `20`; unknown avg `0.03` n `774`
- 1h: commodity avg `-0.0659` n `12`; crypto_alt avg `-0.1487` n `230`; crypto_major avg `-0.0779` n `8`; equity avg `0.0027` n `100`; fx avg `0.0074` n `6`; index avg `0.0055` n `25`; metal avg `-0.0156` n `20`; unknown avg `-0.0506` n `774`
- 4h: commodity avg `-0.0293` n `12`; crypto_alt avg `-0.0985` n `230`; crypto_major avg `-0.2553` n `8`; equity avg `0.0802` n `100`; fx avg `0.0068` n `6`; index avg `0.0281` n `25`; metal avg `-0.0169` n `20`; unknown avg `-0.1182` n `774`
- 24h: commodity avg `-0.6616` n `12`; crypto_alt avg `0.4244` n `230`; crypto_major avg `1.0002` n `8`; equity avg `0.5188` n `100`; fx avg `-0.0273` n `6`; index avg `0.1587` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.2976` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1349`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1229`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1164`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1153`, n `666`, weak_sample_signal
