# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T06:07:24.372465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0128` n `12`; crypto_alt avg `-0.0637` n `230`; crypto_major avg `-0.0749` n `8`; equity avg `-0.0113` n `100`; fx avg `0.0046` n `6`; index avg `0.0013` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.01` n `759`
- 1h: commodity avg `0.0148` n `12`; crypto_alt avg `0.2279` n `230`; crypto_major avg `-0.0491` n `8`; equity avg `-0.0471` n `100`; fx avg `-0.0026` n `6`; index avg `-0.007` n `25`; metal avg `-0.0116` n `20`; unknown avg `0.0065` n `759`
- 4h: commodity avg `-0.1101` n `12`; crypto_alt avg `0.5776` n `230`; crypto_major avg `0.3605` n `8`; equity avg `0.0664` n `100`; fx avg `0.0626` n `6`; index avg `0.0072` n `25`; metal avg `0.0077` n `20`; unknown avg `0.0429` n `758`
- 24h: commodity avg `-0.5213` n `12`; crypto_alt avg `1.311` n `230`; crypto_major avg `1.6646` n `8`; equity avg `0.4351` n `100`; fx avg `0.0693` n `6`; index avg `0.1247` n `25`; metal avg `0.0526` n `20`; unknown avg `-0.1141` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1383`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1231`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.12`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1176`, n `666`, weak_sample_signal
