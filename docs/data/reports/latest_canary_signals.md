# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T09:07:31.188106+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0211` n `12`; crypto_alt avg `0.0354` n `233`; crypto_major avg `0.0633` n `8`; equity avg `0.0288` n `134`; fx avg `-0.0096` n `6`; index avg `0.0017` n `26`; metal avg `-0.0034` n `20`; unknown avg `-0.1772` n `795`
- 1h: commodity avg `0.0546` n `12`; crypto_alt avg `0.134` n `233`; crypto_major avg `0.0519` n `8`; equity avg `-0.1115` n `134`; fx avg `0.0153` n `6`; index avg `-0.0287` n `26`; metal avg `-0.0982` n `20`; unknown avg `-0.1092` n `789`
- 4h: commodity avg `0.1019` n `12`; crypto_alt avg `-0.237` n `233`; crypto_major avg `-0.2494` n `8`; equity avg `-0.2359` n `134`; fx avg `0.0654` n `6`; index avg `-0.0295` n `26`; metal avg `-0.1984` n `20`; unknown avg `-0.338` n `765`
- 24h: commodity avg `-0.0555` n `12`; crypto_alt avg `-4.7716` n `233`; crypto_major avg `-3.2097` n `8`; equity avg `-1.4259` n `134`; fx avg `0.0758` n `6`; index avg `-0.1521` n `26`; metal avg `0.0596` n `20`; unknown avg `-1.0182` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
