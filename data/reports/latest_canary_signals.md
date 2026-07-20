# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T12:22:29.385989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0674` n `12`; crypto_alt avg `-0.0101` n `230`; crypto_major avg `-0.1423` n `8`; equity avg `-0.1635` n `98`; fx avg `-0.0162` n `6`; index avg `-0.0047` n `25`; metal avg `-0.065` n `20`; unknown avg `0.0061` n `770`
- 1h: commodity avg `0.1059` n `12`; crypto_alt avg `0.3785` n `230`; crypto_major avg `0.4546` n `8`; equity avg `-0.0003` n `98`; fx avg `-0.0281` n `6`; index avg `-0.0061` n `25`; metal avg `-0.1069` n `20`; unknown avg `0.1471` n `770`
- 4h: commodity avg `0.1328` n `12`; crypto_alt avg `0.7229` n `230`; crypto_major avg `0.7194` n `8`; equity avg `0.4626` n `98`; fx avg `-0.0459` n `6`; index avg `0.1305` n `25`; metal avg `-0.1442` n `20`; unknown avg `0.0803` n `769`
- 24h: commodity avg `-0.4569` n `12`; crypto_alt avg `0.9315` n `230`; crypto_major avg `0.4764` n `8`; equity avg `0.844` n `97`; fx avg `-0.0604` n `6`; index avg `0.1783` n `25`; metal avg `0.1438` n `20`; unknown avg `-0.0126` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1092`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.105`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1022`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0907`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0763`, n `666`, weak_sample_signal
