# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T19:07:30.740474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.042` n `13`; crypto_alt avg `0.0173` n `235`; crypto_major avg `-0.0254` n `8`; equity avg `-0.0023` n `143`; fx avg `0.001` n `6`; index avg `0.0019` n `26`; metal avg `0.0011` n `20`; unknown avg `4.8703` n `1076`
- 1h: commodity avg `0.0467` n `13`; crypto_alt avg `-0.1991` n `235`; crypto_major avg `-0.157` n `8`; equity avg `-0.0111` n `143`; fx avg `-0.006` n `6`; index avg `0.0064` n `26`; metal avg `-0.0013` n `20`; unknown avg `4.8015` n `1076`
- 4h: commodity avg `-0.0158` n `13`; crypto_alt avg `0.1133` n `235`; crypto_major avg `0.2622` n `8`; equity avg `0.0863` n `143`; fx avg `-0.0111` n `6`; index avg `0.0265` n `26`; metal avg `0.0001` n `20`; unknown avg `1.3183` n `1038`
- 24h: commodity avg `0.2221` n `13`; crypto_alt avg `2.5239` n `235`; crypto_major avg `1.3655` n `8`; equity avg `0.2628` n `143`; fx avg `-0.0486` n `6`; index avg `0.0735` n `26`; metal avg `0.0163` n `20`; unknown avg `1.1519` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1896`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
