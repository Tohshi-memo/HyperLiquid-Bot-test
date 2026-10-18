# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T03:07:35.938419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `13`; crypto_alt avg `0.267` n `237`; crypto_major avg `0.1814` n `8`; equity avg `0.0731` n `151`; fx avg `-0.0052` n `6`; index avg `0.0076` n `26`; metal avg `0.0075` n `20`; unknown avg `0.0743` n `1191`
- 1h: commodity avg `0.0123` n `13`; crypto_alt avg `0.2129` n `237`; crypto_major avg `0.3504` n `8`; equity avg `0.0911` n `151`; fx avg `-0.0136` n `6`; index avg `0.0154` n `26`; metal avg `0.009` n `20`; unknown avg `0.0739` n `1191`
- 4h: commodity avg `0.0091` n `13`; crypto_alt avg `0.2747` n `236`; crypto_major avg `0.8282` n `8`; equity avg `0.1974` n `151`; fx avg `-0.0103` n `6`; index avg `0.0443` n `26`; metal avg `0.0347` n `20`; unknown avg `0.201` n `1185`
- 24h: commodity avg `-0.0965` n `13`; crypto_alt avg `-1.9279` n `236`; crypto_major avg `-0.1833` n `8`; equity avg `-0.8736` n `151`; fx avg `-0.0422` n `6`; index avg `-0.1047` n `26`; metal avg `-0.0578` n `20`; unknown avg `3.5908` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1636`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.137`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.108`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0757`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
