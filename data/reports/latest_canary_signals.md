# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T15:37:33.178407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `13`; crypto_alt avg `-0.008` n `235`; crypto_major avg `-0.0732` n `8`; equity avg `0.006` n `143`; fx avg `0.0007` n `6`; index avg `0.0017` n `26`; metal avg `0.0013` n `20`; unknown avg `-0.0573` n `1078`
- 1h: commodity avg `0.025` n `13`; crypto_alt avg `0.0102` n `235`; crypto_major avg `0.1296` n `8`; equity avg `0.0201` n `143`; fx avg `0.0041` n `6`; index avg `0.0049` n `26`; metal avg `0.0053` n `20`; unknown avg `-0.1169` n `972`
- 4h: commodity avg `0.1832` n `13`; crypto_alt avg `0.3433` n `235`; crypto_major avg `0.3207` n `8`; equity avg `0.0274` n `143`; fx avg `-0.0099` n `6`; index avg `0.015` n `26`; metal avg `-0.0134` n `20`; unknown avg `0.0972` n `946`
- 24h: commodity avg `0.6999` n `13`; crypto_alt avg `-1.2316` n `235`; crypto_major avg `-0.6436` n `8`; equity avg `0.0614` n `143`; fx avg `-0.0317` n `6`; index avg `0.0395` n `26`; metal avg `0.0685` n `20`; unknown avg `0.2212` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1966`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
