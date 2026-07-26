# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T11:22:27.883477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `12`; crypto_alt avg `0.0524` n `230`; crypto_major avg `0.0303` n `8`; equity avg `0.0069` n `100`; fx avg `-0.0064` n `6`; index avg `-0.0122` n `25`; metal avg `0.008` n `20`; unknown avg `-0.004` n `775`
- 1h: commodity avg `-0.0037` n `12`; crypto_alt avg `0.0227` n `230`; crypto_major avg `0.0232` n `8`; equity avg `0.1058` n `100`; fx avg `-0.0025` n `6`; index avg `-0.006` n `25`; metal avg `0.0696` n `20`; unknown avg `0.0623` n `775`
- 4h: commodity avg `-0.2773` n `12`; crypto_alt avg `-0.0113` n `230`; crypto_major avg `0.0639` n `8`; equity avg `0.212` n `100`; fx avg `-0.039` n `6`; index avg `0.0447` n `25`; metal avg `0.1466` n `20`; unknown avg `-0.0035` n `775`
- 24h: commodity avg `-0.8156` n `12`; crypto_alt avg `1.5954` n `230`; crypto_major avg `1.661` n `8`; equity avg `0.767` n `100`; fx avg `0.0158` n `6`; index avg `0.1569` n `25`; metal avg `0.1974` n `20`; unknown avg `0.1439` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.147`, n `667`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1357`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1317`, n `667`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1254`, n `667`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1253`, n `667`, weak_sample_signal
