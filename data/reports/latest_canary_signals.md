# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T20:07:26.747889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `13`; crypto_alt avg `-0.1848` n `239`; crypto_major avg `-0.1744` n `8`; equity avg `-0.089` n `162`; fx avg `0.007` n `6`; index avg `-0.0186` n `27`; metal avg `0.004` n `20`; unknown avg `1.4443` n `1251`
- 1h: commodity avg `0.0197` n `13`; crypto_alt avg `0.0982` n `239`; crypto_major avg `0.2065` n `8`; equity avg `0.1045` n `162`; fx avg `0.0206` n `6`; index avg `0.0117` n `27`; metal avg `0.0343` n `20`; unknown avg `1.2583` n `1253`
- 4h: commodity avg `0.0541` n `13`; crypto_alt avg `0.1306` n `239`; crypto_major avg `0.2547` n `8`; equity avg `0.403` n `162`; fx avg `0.0549` n `6`; index avg `0.0239` n `27`; metal avg `0.0884` n `20`; unknown avg `25.5785` n `1251`
- 24h: commodity avg `0.0862` n `13`; crypto_alt avg `-0.0754` n `239`; crypto_major avg `-0.023` n `8`; equity avg `0.4686` n `162`; fx avg `0.0471` n `6`; index avg `0.0654` n `27`; metal avg `-0.0476` n `20`; unknown avg `3.1603` n `1140`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
