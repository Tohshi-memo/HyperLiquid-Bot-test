# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T16:52:23.830414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `-0.1147` n `230`; crypto_major avg `-0.0834` n `8`; equity avg `-0.0148` n `100`; fx avg `-0.0015` n `6`; index avg `0.0079` n `25`; metal avg `-0.0093` n `20`; unknown avg `0.0555` n `775`
- 1h: commodity avg `0.0082` n `12`; crypto_alt avg `0.085` n `230`; crypto_major avg `0.1722` n `8`; equity avg `0.0463` n `100`; fx avg `0.0009` n `6`; index avg `0.0307` n `25`; metal avg `0.0468` n `20`; unknown avg `-0.1569` n `775`
- 4h: commodity avg `0.0249` n `12`; crypto_alt avg `0.3213` n `230`; crypto_major avg `0.608` n `8`; equity avg `0.2033` n `100`; fx avg `-0.0196` n `6`; index avg `0.0465` n `25`; metal avg `0.0229` n `20`; unknown avg `0.1315` n `775`
- 24h: commodity avg `-0.4655` n `12`; crypto_alt avg `1.2262` n `230`; crypto_major avg `1.3414` n `8`; equity avg `0.9016` n `100`; fx avg `0.0137` n `6`; index avg `0.219` n `25`; metal avg `0.2117` n `20`; unknown avg `0.0552` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1928`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
