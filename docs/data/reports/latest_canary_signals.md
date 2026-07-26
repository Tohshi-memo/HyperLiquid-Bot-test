# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T21:09:21.129122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0618` n `12`; crypto_alt avg `0.022` n `230`; crypto_major avg `0.0006` n `8`; equity avg `0.0245` n `100`; fx avg `-0.0131` n `6`; index avg `-0.0012` n `25`; metal avg `0.02` n `20`; unknown avg `0.0185` n `775`
- 1h: commodity avg `0.0449` n `12`; crypto_alt avg `-0.0817` n `230`; crypto_major avg `-0.0712` n `8`; equity avg `0.0666` n `100`; fx avg `-0.0023` n `6`; index avg `-0.0024` n `25`; metal avg `0.0192` n `20`; unknown avg `0.0909` n `775`
- 4h: commodity avg `0.2802` n `12`; crypto_alt avg `-0.2568` n `230`; crypto_major avg `-0.2365` n `8`; equity avg `-0.0363` n `100`; fx avg `0.028` n `6`; index avg `-0.0417` n `25`; metal avg `0.0258` n `20`; unknown avg `-0.0818` n `775`
- 24h: commodity avg `-0.1431` n `12`; crypto_alt avg `0.8094` n `230`; crypto_major avg `0.86` n `8`; equity avg `0.6347` n `100`; fx avg `0.0384` n `6`; index avg `0.0969` n `25`; metal avg `0.2093` n `20`; unknown avg `-0.0779` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
