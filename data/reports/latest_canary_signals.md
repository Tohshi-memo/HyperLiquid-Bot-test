# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T04:37:23.199719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0301` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0854` n `12`; crypto_alt avg `0.0653` n `228`; crypto_major avg `-0.0445` n `8`; equity avg `0.0019` n `69`; fx avg `0.0061` n `6`; index avg `0.0163` n `23`; metal avg `-0.0138` n `18`; unknown avg `-0.2065` n `422`
- 1h: commodity avg `0.1642` n `12`; crypto_alt avg `-0.6773` n `228`; crypto_major avg `-0.6905` n `8`; equity avg `-0.1368` n `69`; fx avg `-0.0236` n `6`; index avg `-0.009` n `23`; metal avg `-0.0851` n `18`; unknown avg `-0.4262` n `422`
- 4h: commodity avg `0.1199` n `12`; crypto_alt avg `-0.2886` n `228`; crypto_major avg `-0.7515` n `8`; equity avg `0.0662` n `69`; fx avg `0.0346` n `6`; index avg `0.2786` n `23`; metal avg `-0.0521` n `18`; unknown avg `-0.5481` n `421`
- 24h: commodity avg `0.951` n `12`; crypto_alt avg `0.4595` n `228`; crypto_major avg `-0.9048` n `8`; equity avg `0.5338` n `69`; fx avg `0.0223` n `6`; index avg `0.7191` n `23`; metal avg `0.1805` n `18`; unknown avg `1.582` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2884`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2245`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2035`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
