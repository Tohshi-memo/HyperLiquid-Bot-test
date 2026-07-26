# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T03:37:24.953700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `12`; crypto_alt avg `0.0234` n `230`; crypto_major avg `0.0642` n `8`; equity avg `0.039` n `100`; fx avg `-0.0028` n `6`; index avg `0.0012` n `25`; metal avg `0.0031` n `20`; unknown avg `0.4663` n `775`
- 1h: commodity avg `-0.0463` n `12`; crypto_alt avg `0.2622` n `230`; crypto_major avg `0.1649` n `8`; equity avg `0.0968` n `100`; fx avg `0.0076` n `6`; index avg `0.0021` n `25`; metal avg `0.003` n `20`; unknown avg `0.1361` n `774`
- 4h: commodity avg `-0.0013` n `12`; crypto_alt avg `0.4468` n `230`; crypto_major avg `0.4453` n `8`; equity avg `0.2212` n `100`; fx avg `0.0043` n `6`; index avg `0.0385` n `25`; metal avg `0.0201` n `20`; unknown avg `-0.1731` n `774`
- 24h: commodity avg `-0.49` n `12`; crypto_alt avg `0.8021` n `230`; crypto_major avg `1.3522` n `8`; equity avg `0.5035` n `100`; fx avg `0.0053` n `6`; index avg `0.1357` n `25`; metal avg `0.0417` n `20`; unknown avg `-0.2246` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1376`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1241`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1181`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
