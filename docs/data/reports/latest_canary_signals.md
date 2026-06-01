# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T05:22:21.796664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1247` n `12`; crypto_alt avg `0.1357` n `228`; crypto_major avg `0.1342` n `8`; equity avg `-0.0237` n `69`; fx avg `-0.0019` n `6`; index avg `-0.1969` n `23`; metal avg `0.1365` n `18`; unknown avg `-0.2193` n `422`
- 1h: commodity avg `-0.1285` n `12`; crypto_alt avg `-0.0217` n `228`; crypto_major avg `0.2008` n `8`; equity avg `0.0546` n `69`; fx avg `-0.005` n `6`; index avg `-0.1058` n `23`; metal avg `0.2032` n `18`; unknown avg `-0.5758` n `422`
- 4h: commodity avg `-0.033` n `12`; crypto_alt avg `0.039` n `228`; crypto_major avg `-0.1899` n `8`; equity avg `0.2367` n `69`; fx avg `-0.0022` n `6`; index avg `0.2213` n `23`; metal avg `0.1584` n `18`; unknown avg `-0.471` n `421`
- 24h: commodity avg `0.9405` n `12`; crypto_alt avg `0.3465` n `228`; crypto_major avg `-0.7197` n `8`; equity avg `0.5337` n `69`; fx avg `0.0323` n `6`; index avg `0.5742` n `23`; metal avg `0.3784` n `18`; unknown avg `1.6676` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2872`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2246`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2037`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
