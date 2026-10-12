# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T02:52:32.280815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0124` n `13`; crypto_alt avg `0.0069` n `235`; crypto_major avg `-0.08` n `8`; equity avg `-0.0048` n `151`; fx avg `0.0091` n `6`; index avg `-0.0026` n `26`; metal avg `-0.024` n `20`; unknown avg `0.2446` n `1133`
- 1h: commodity avg `-0.0487` n `13`; crypto_alt avg `0.8873` n `235`; crypto_major avg `0.5015` n `8`; equity avg `-0.4785` n `151`; fx avg `-0.0116` n `6`; index avg `-0.0012` n `26`; metal avg `0.0036` n `20`; unknown avg `0.4132` n `1111`
- 4h: commodity avg `-0.5816` n `13`; crypto_alt avg `0.2617` n `235`; crypto_major avg `0.3378` n `8`; equity avg `-0.5404` n `151`; fx avg `-0.0476` n `6`; index avg `-0.0071` n `26`; metal avg `0.1664` n `20`; unknown avg `0.684` n `1089`
- 24h: commodity avg `-0.4269` n `13`; crypto_alt avg `2.0695` n `235`; crypto_major avg `1.0335` n `8`; equity avg `-0.246` n `151`; fx avg `-0.0518` n `6`; index avg `0.022` n `26`; metal avg `0.1769` n `20`; unknown avg `0.8326` n `928`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
