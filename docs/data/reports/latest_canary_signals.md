# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T07:22:28.005858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.2557` n `230`; crypto_major avg `-0.1765` n `8`; equity avg `-0.094` n `93`; fx avg `0.0076` n `6`; index avg `-0.0188` n `25`; metal avg `-0.0345` n `20`; unknown avg `-0.0205` n `767`
- 1h: commodity avg `0.1365` n `12`; crypto_alt avg `-0.4194` n `230`; crypto_major avg `-0.5301` n `8`; equity avg `-0.061` n `93`; fx avg `0.0252` n `6`; index avg `-0.0163` n `25`; metal avg `0.0767` n `20`; unknown avg `-0.1703` n `767`
- 4h: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.2141` n `230`; crypto_major avg `0.0162` n `8`; equity avg `-0.0127` n `93`; fx avg `0.0155` n `6`; index avg `-0.0322` n `25`; metal avg `0.0122` n `20`; unknown avg `0.0737` n `749`
- 24h: commodity avg `0.0183` n `12`; crypto_alt avg `1.2608` n `230`; crypto_major avg `3.0901` n `8`; equity avg `1.5967` n `92`; fx avg `0.0979` n `6`; index avg `0.4603` n `25`; metal avg `0.2485` n `20`; unknown avg `0.225` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
