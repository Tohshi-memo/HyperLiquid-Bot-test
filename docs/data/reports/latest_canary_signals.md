# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T11:13:29.171487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0694` n `12`; crypto_alt avg `-0.0491` n `230`; crypto_major avg `-0.0416` n `8`; equity avg `0.0148` n `113`; fx avg `-0.0096` n `6`; index avg `0.0159` n `25`; metal avg `0.0713` n `20`; unknown avg `0.0123` n `786`
- 1h: commodity avg `0.0398` n `12`; crypto_alt avg `-0.0401` n `230`; crypto_major avg `0.0156` n `8`; equity avg `-0.04` n `113`; fx avg `0.0029` n `6`; index avg `-0.0055` n `25`; metal avg `0.0411` n `20`; unknown avg `0.0172` n `786`
- 4h: commodity avg `-0.0677` n `12`; crypto_alt avg `-0.0388` n `230`; crypto_major avg `0.4414` n `8`; equity avg `0.462` n `113`; fx avg `-0.0438` n `6`; index avg `0.0769` n `25`; metal avg `0.2135` n `20`; unknown avg `-0.087` n `786`
- 24h: commodity avg `0.3457` n `12`; crypto_alt avg `-1.1457` n `230`; crypto_major avg `0.6973` n `8`; equity avg `2.0137` n `113`; fx avg `0.0478` n `6`; index avg `0.1546` n `25`; metal avg `0.1752` n `20`; unknown avg `-0.1976` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2448`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2339`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1959`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
