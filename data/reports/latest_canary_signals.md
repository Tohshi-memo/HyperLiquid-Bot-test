# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T19:45:18.570878+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0152` n `12`; crypto_alt avg `0.0602` n `230`; crypto_major avg `0.033` n `8`; equity avg `0.1761` n `92`; fx avg `0.0054` n `6`; index avg `0.0232` n `25`; metal avg `0.0336` n `20`; unknown avg `0.0102` n `766`
- 1h: commodity avg `0.0775` n `12`; crypto_alt avg `0.0465` n `230`; crypto_major avg `0.137` n `8`; equity avg `-0.0785` n `92`; fx avg `0.0011` n `6`; index avg `-0.0515` n `25`; metal avg `-0.0313` n `20`; unknown avg `-0.0491` n `766`
- 4h: commodity avg `0.6408` n `12`; crypto_alt avg `-0.8065` n `230`; crypto_major avg `-0.5386` n `8`; equity avg `-0.8601` n `92`; fx avg `-0.0058` n `6`; index avg `-0.1592` n `25`; metal avg `-0.1634` n `20`; unknown avg `-0.09` n `766`
- 24h: commodity avg `0.628` n `12`; crypto_alt avg `-2.3846` n `230`; crypto_major avg `-3.0539` n `8`; equity avg `-3.3238` n `92`; fx avg `-0.0789` n `6`; index avg `-0.6629` n `25`; metal avg `-0.5563` n `20`; unknown avg `-0.2908` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
