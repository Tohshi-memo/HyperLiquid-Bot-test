# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T19:37:27.148856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0145` n `13`; crypto_alt avg `0.0879` n `235`; crypto_major avg `0.0403` n `8`; equity avg `0.0073` n `144`; fx avg `-0.0009` n `6`; index avg `-0.0022` n `26`; metal avg `0.0063` n `20`; unknown avg `-0.1405` n `1078`
- 1h: commodity avg `-0.0212` n `13`; crypto_alt avg `0.2486` n `235`; crypto_major avg `0.1199` n `8`; equity avg `-0.0013` n `144`; fx avg `0.0025` n `6`; index avg `-0.0012` n `26`; metal avg `0.0089` n `20`; unknown avg `0.1299` n `1076`
- 4h: commodity avg `0.0131` n `13`; crypto_alt avg `0.4067` n `235`; crypto_major avg `0.3923` n `8`; equity avg `0.01` n `144`; fx avg `-0.0247` n `6`; index avg `0.0002` n `26`; metal avg `0.0155` n `20`; unknown avg `0.3982` n `1068`
- 24h: commodity avg `-0.002` n `13`; crypto_alt avg `1.2676` n `235`; crypto_major avg `1.1434` n `8`; equity avg `0.185` n `144`; fx avg `0.028` n `6`; index avg `-0.022` n `26`; metal avg `0.0058` n `20`; unknown avg `0.4459` n `1023`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
