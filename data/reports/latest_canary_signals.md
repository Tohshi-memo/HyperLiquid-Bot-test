# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T07:52:30.536359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0224` n `12`; crypto_alt avg `-0.0544` n `230`; crypto_major avg `-0.0941` n `8`; equity avg `0.0217` n `112`; fx avg `0.0012` n `6`; index avg `0.003` n `25`; metal avg `0.0058` n `20`; unknown avg `0.0105` n `785`
- 1h: commodity avg `0.0565` n `12`; crypto_alt avg `0.0659` n `230`; crypto_major avg `0.1939` n `8`; equity avg `0.2012` n `112`; fx avg `0.009` n `6`; index avg `0.0273` n `25`; metal avg `0.0109` n `20`; unknown avg `0.0578` n `785`
- 4h: commodity avg `-0.0984` n `12`; crypto_alt avg `0.2803` n `230`; crypto_major avg `0.4252` n `8`; equity avg `0.2541` n `112`; fx avg `0.0981` n `6`; index avg `0.0534` n `25`; metal avg `0.1562` n `20`; unknown avg `57.1591` n `753`
- 24h: commodity avg `0.2894` n `12`; crypto_alt avg `1.0188` n `230`; crypto_major avg `0.2773` n `8`; equity avg `0.0295` n `112`; fx avg `0.2076` n `6`; index avg `0.0714` n `25`; metal avg `-0.028` n `20`; unknown avg `56.9027` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
