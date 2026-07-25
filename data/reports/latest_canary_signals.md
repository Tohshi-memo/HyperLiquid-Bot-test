# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T19:53:59.434592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0439` n `12`; crypto_alt avg `0.0674` n `230`; crypto_major avg `0.0269` n `8`; equity avg `0.0099` n `100`; fx avg `-0.0065` n `6`; index avg `0.0094` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0072` n `774`
- 1h: commodity avg `-0.0525` n `12`; crypto_alt avg `-0.0087` n `230`; crypto_major avg `-0.1325` n `8`; equity avg `0.0282` n `100`; fx avg `0.0223` n `6`; index avg `0.0023` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.0778` n `774`
- 4h: commodity avg `-0.0437` n `12`; crypto_alt avg `0.3179` n `230`; crypto_major avg `0.5773` n `8`; equity avg `0.2077` n `100`; fx avg `-0.0058` n `6`; index avg `0.0544` n `25`; metal avg `0.0108` n `20`; unknown avg `-0.1204` n `774`
- 24h: commodity avg `-0.3937` n `12`; crypto_alt avg `0.5157` n `230`; crypto_major avg `1.1404` n `8`; equity avg `0.5495` n `100`; fx avg `-0.0107` n `6`; index avg `0.1499` n `25`; metal avg `0.0269` n `20`; unknown avg `-0.2972` n `757`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1325`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.119`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1146`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1117`, n `666`, weak_sample_signal
