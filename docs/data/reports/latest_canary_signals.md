# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T23:24:51.624869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `-0.1267` n `230`; crypto_major avg `-0.0801` n `8`; equity avg `0.0073` n `100`; fx avg `0.0235` n `6`; index avg `0.0042` n `25`; metal avg `0.0019` n `20`; unknown avg `-0.0009` n `774`
- 1h: commodity avg `-0.0639` n `12`; crypto_alt avg `-0.1632` n `230`; crypto_major avg `-0.0781` n `8`; equity avg `0.0019` n `100`; fx avg `0.0048` n `6`; index avg `0.005` n `25`; metal avg `-0.014` n `20`; unknown avg `-0.0742` n `774`
- 4h: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.1128` n `230`; crypto_major avg `-0.2556` n `8`; equity avg `0.0793` n `100`; fx avg `0.0042` n `6`; index avg `0.0276` n `25`; metal avg `-0.0154` n `20`; unknown avg `-0.1384` n `774`
- 24h: commodity avg `-0.6597` n `12`; crypto_alt avg `0.4098` n `230`; crypto_major avg `1.0001` n `8`; equity avg `0.518` n `100`; fx avg `-0.0298` n `6`; index avg `0.1582` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.3096` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1349`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1229`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1164`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1153`, n `666`, weak_sample_signal
