# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T18:22:25.190552+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `13`; crypto_alt avg `-0.0637` n `237`; crypto_major avg `-0.123` n `8`; equity avg `0.0146` n `151`; fx avg `0.0022` n `6`; index avg `-0.0062` n `26`; metal avg `-0.0042` n `20`; unknown avg `-0.2145` n `1192`
- 1h: commodity avg `-0.0147` n `13`; crypto_alt avg `-0.3299` n `237`; crypto_major avg `-0.1363` n `8`; equity avg `-0.0356` n `151`; fx avg `0.0042` n `6`; index avg `-0.0191` n `26`; metal avg `0.0007` n `20`; unknown avg `-0.576` n `1188`
- 4h: commodity avg `-0.0006` n `13`; crypto_alt avg `-1.0906` n `237`; crypto_major avg `-0.6969` n `8`; equity avg `-0.2854` n `151`; fx avg `0.0149` n `6`; index avg `-0.046` n `26`; metal avg `-0.0025` n `20`; unknown avg `-0.8161` n `1159`
- 24h: commodity avg `-0.0365` n `13`; crypto_alt avg `-3.4737` n `236`; crypto_major avg `-1.4604` n `8`; equity avg `-0.9867` n `151`; fx avg `0.0105` n `6`; index avg `-0.1219` n `26`; metal avg `-0.045` n `20`; unknown avg `0.2223` n `1015`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2108`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1407`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1315`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1101`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0804`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
