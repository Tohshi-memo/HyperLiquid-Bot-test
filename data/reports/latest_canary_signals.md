# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T03:22:27.668565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0325` n `13`; crypto_alt avg `0.024` n `235`; crypto_major avg `-0.0163` n `8`; equity avg `-0.036` n `151`; fx avg `-0.0085` n `6`; index avg `-0.0027` n `26`; metal avg `-0.0069` n `20`; unknown avg `0.4567` n `1133`
- 1h: commodity avg `-0.0439` n `13`; crypto_alt avg `0.0952` n `235`; crypto_major avg `-0.1274` n `8`; equity avg `-0.6177` n `151`; fx avg `-0.0255` n `6`; index avg `-0.018` n `26`; metal avg `-0.0781` n `20`; unknown avg `-0.0085` n `1111`
- 4h: commodity avg `-0.4603` n `13`; crypto_alt avg `0.1081` n `235`; crypto_major avg `0.2016` n `8`; equity avg `-0.6768` n `151`; fx avg `-0.0718` n `6`; index avg `-0.0532` n `26`; metal avg `0.0846` n `20`; unknown avg `0.3674` n `1097`
- 24h: commodity avg `-0.5538` n `13`; crypto_alt avg `2.8343` n `235`; crypto_major avg `1.2299` n `8`; equity avg `-0.2495` n `151`; fx avg `-0.0785` n `6`; index avg `0.0121` n `26`; metal avg `0.1508` n `20`; unknown avg `0.7651` n `928`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
