# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T00:52:33.915206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0545` n `13`; crypto_alt avg `-0.1053` n `235`; crypto_major avg `-0.0738` n `8`; equity avg `-0.0128` n `143`; fx avg `0.0` n `6`; index avg `-0.0015` n `26`; metal avg `0.0` n `20`; unknown avg `-0.1069` n `1079`
- 1h: commodity avg `-0.0345` n `13`; crypto_alt avg `-0.1339` n `235`; crypto_major avg `0.0859` n `8`; equity avg `-0.0195` n `143`; fx avg `0.0` n `6`; index avg `-0.0042` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.0238` n `1071`
- 4h: commodity avg `0.0105` n `13`; crypto_alt avg `0.0974` n `235`; crypto_major avg `0.0111` n `8`; equity avg `0.0409` n `143`; fx avg `0.0041` n `6`; index avg `0.0003` n `26`; metal avg `0.0004` n `20`; unknown avg `-0.3109` n `1055`
- 24h: commodity avg `-0.0243` n `13`; crypto_alt avg `1.2492` n `235`; crypto_major avg `0.3464` n `8`; equity avg `0.1611` n `143`; fx avg `-0.0156` n `6`; index avg `0.0344` n `26`; metal avg `-0.0127` n `20`; unknown avg `-0.0486` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1989`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
