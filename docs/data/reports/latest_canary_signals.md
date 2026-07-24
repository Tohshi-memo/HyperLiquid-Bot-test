# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T22:07:27.114999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0498` n `12`; crypto_alt avg `-0.1261` n `230`; crypto_major avg `0.0134` n `8`; equity avg `-0.0013` n `100`; fx avg `-0.0014` n `6`; index avg `-0.0142` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.0354` n `774`
- 1h: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.1616` n `230`; crypto_major avg `-0.1775` n `8`; equity avg `-0.0235` n `100`; fx avg `0.0068` n `6`; index avg `-0.0081` n `25`; metal avg `0.0126` n `20`; unknown avg `-0.1256` n `774`
- 4h: commodity avg `0.3652` n `12`; crypto_alt avg `-0.5155` n `230`; crypto_major avg `-0.433` n `8`; equity avg `-0.7553` n `100`; fx avg `-0.0061` n `6`; index avg `-0.1641` n `25`; metal avg `-0.0993` n `20`; unknown avg `-0.0839` n `773`
- 24h: commodity avg `-0.3005` n `12`; crypto_alt avg `-1.2874` n `230`; crypto_major avg `-1.2473` n `8`; equity avg `-3.2137` n `100`; fx avg `-0.1633` n `6`; index avg `-0.4523` n `25`; metal avg `0.0137` n `20`; unknown avg `13.9918` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1268`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1217`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1119`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1101`, n `666`, weak_sample_signal
