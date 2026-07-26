# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T06:52:25.925778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0939` n `12`; crypto_alt avg `0.1284` n `230`; crypto_major avg `0.1533` n `8`; equity avg `0.0723` n `100`; fx avg `0.0` n `6`; index avg `0.0043` n `25`; metal avg `0.004` n `20`; unknown avg `0.0086` n `775`
- 1h: commodity avg `0.1216` n `12`; crypto_alt avg `-0.0232` n `230`; crypto_major avg `-0.0155` n `8`; equity avg `0.0633` n `100`; fx avg `0.0056` n `6`; index avg `0.0011` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0052` n `759`
- 4h: commodity avg `0.0343` n `12`; crypto_alt avg `0.4178` n `230`; crypto_major avg `0.2325` n `8`; equity avg `0.0983` n `100`; fx avg `0.0654` n `6`; index avg `0.0081` n `25`; metal avg `0.0099` n `20`; unknown avg `0.0104` n `758`
- 24h: commodity avg `-0.4332` n `12`; crypto_alt avg `1.5912` n `230`; crypto_major avg `1.7776` n `8`; equity avg `0.502` n `100`; fx avg `0.0598` n `6`; index avg `0.1186` n `25`; metal avg `0.0489` n `20`; unknown avg `-0.0951` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1386`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1233`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1209`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
