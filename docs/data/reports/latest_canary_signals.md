# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T06:22:47.405544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `-0.1087` n `234`; crypto_major avg `0.0616` n `8`; equity avg `-0.0146` n `140`; fx avg `-0.0152` n `6`; index avg `-0.0001` n `26`; metal avg `0.0088` n `20`; unknown avg `2.9913` n `943`
- 1h: commodity avg `0.0061` n `12`; crypto_alt avg `0.0576` n `234`; crypto_major avg `0.0299` n `8`; equity avg `-0.0028` n `140`; fx avg `0.0016` n `6`; index avg `0.001` n `26`; metal avg `0.0102` n `20`; unknown avg `1.1535` n `911`
- 4h: commodity avg `0.0889` n `12`; crypto_alt avg `-1.5815` n `234`; crypto_major avg `-1.0787` n `8`; equity avg `-0.4717` n `140`; fx avg `-0.0164` n `6`; index avg `-0.0819` n `26`; metal avg `-0.015` n `20`; unknown avg `5.0094` n `895`
- 24h: commodity avg `0.2276` n `12`; crypto_alt avg `0.4465` n `234`; crypto_major avg `-1.5999` n `8`; equity avg `-0.1861` n `140`; fx avg `-0.0679` n `6`; index avg `-0.0299` n `26`; metal avg `0.013` n `20`; unknown avg `3.0931` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
