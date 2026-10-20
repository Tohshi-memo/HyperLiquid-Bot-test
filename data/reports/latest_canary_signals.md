# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T08:52:29.710232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0359` n `13`; crypto_alt avg `-0.2086` n `237`; crypto_major avg `-0.1778` n `8`; equity avg `-0.213` n `151`; fx avg `-0.0034` n `6`; index avg `-0.063` n `26`; metal avg `-0.0396` n `20`; unknown avg `-0.1072` n `1198`
- 1h: commodity avg `0.0971` n `13`; crypto_alt avg `-0.4471` n `237`; crypto_major avg `-0.2453` n `8`; equity avg `0.0086` n `151`; fx avg `0.0051` n `6`; index avg `-0.0127` n `26`; metal avg `0.0484` n `20`; unknown avg `-0.1354` n `1180`
- 4h: commodity avg `0.2278` n `13`; crypto_alt avg `-0.8056` n `237`; crypto_major avg `-0.8112` n `8`; equity avg `-0.2961` n `151`; fx avg `-0.0055` n `6`; index avg `-0.023` n `26`; metal avg `-0.0781` n `20`; unknown avg `5.3287` n `1160`
- 24h: commodity avg `0.4437` n `13`; crypto_alt avg `-0.5869` n `237`; crypto_major avg `-1.2154` n `8`; equity avg `-1.508` n `151`; fx avg `0.0031` n `6`; index avg `-0.2305` n `26`; metal avg `-0.1727` n `20`; unknown avg `4.6392` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
