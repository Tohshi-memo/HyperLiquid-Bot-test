# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T20:37:32.141731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0717` n `12`; crypto_alt avg `-0.0339` n `230`; crypto_major avg `-0.0826` n `8`; equity avg `-0.0817` n `100`; fx avg `-0.0081` n `6`; index avg `-0.0236` n `25`; metal avg `0.013` n `20`; unknown avg `-0.0393` n `774`
- 1h: commodity avg `0.2726` n `12`; crypto_alt avg `0.0564` n `230`; crypto_major avg `-0.1196` n `8`; equity avg `0.0056` n `100`; fx avg `-0.0139` n `6`; index avg `-0.0256` n `25`; metal avg `-0.0053` n `20`; unknown avg `-0.0387` n `773`
- 4h: commodity avg `0.3186` n `12`; crypto_alt avg `0.1636` n `230`; crypto_major avg `0.1299` n `8`; equity avg `-1.196` n `100`; fx avg `-0.0398` n `6`; index avg `-0.2288` n `25`; metal avg `-0.1808` n `20`; unknown avg `-0.1699` n `773`
- 24h: commodity avg `-0.2561` n `12`; crypto_alt avg `-1.1965` n `230`; crypto_major avg `-1.1289` n `8`; equity avg `-3.5444` n `100`; fx avg `-0.1815` n `6`; index avg `-0.5274` n `25`; metal avg `-0.0162` n `20`; unknown avg `13.8737` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1293`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1251`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1159`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1118`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `666`, weak_sample_signal
