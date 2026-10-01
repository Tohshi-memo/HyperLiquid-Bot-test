# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T23:07:27.928763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0217` n `13`; crypto_alt avg `0.1219` n `234`; crypto_major avg `0.0434` n `8`; equity avg `0.0794` n `142`; fx avg `-0.0102` n `6`; index avg `0.0205` n `26`; metal avg `0.004` n `20`; unknown avg `0.0504` n `983`
- 1h: commodity avg `-0.041` n `13`; crypto_alt avg `-0.167` n `234`; crypto_major avg `-0.079` n `8`; equity avg `0.0953` n `142`; fx avg `-0.0127` n `6`; index avg `0.016` n `26`; metal avg `0.0075` n `20`; unknown avg `-0.057` n `983`
- 4h: commodity avg `0.0158` n `13`; crypto_alt avg `-0.5595` n `234`; crypto_major avg `-0.3981` n `8`; equity avg `0.1002` n `142`; fx avg `0.0067` n `6`; index avg `0.0324` n `26`; metal avg `0.0533` n `20`; unknown avg `-0.3477` n `891`
- 24h: commodity avg `0.0956` n `13`; crypto_alt avg `-0.8409` n `234`; crypto_major avg `-0.4367` n `8`; equity avg `1.0295` n `142`; fx avg `-0.1131` n `6`; index avg `0.1821` n `26`; metal avg `0.0057` n `20`; unknown avg `0.3659` n `816`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
