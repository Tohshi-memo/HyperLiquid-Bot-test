# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T18:17:59.039693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `13`; crypto_alt avg `-0.0606` n `239`; crypto_major avg `-0.0769` n `8`; equity avg `-0.0046` n `166`; fx avg `0.0088` n `6`; index avg `0.0056` n `27`; metal avg `0.001` n `20`; unknown avg `-0.2285` n `1258`
- 1h: commodity avg `0.0154` n `13`; crypto_alt avg `-0.0889` n `239`; crypto_major avg `-0.0795` n `8`; equity avg `0.0252` n `166`; fx avg `0.0039` n `6`; index avg `-0.0723` n `27`; metal avg `0.0009` n `20`; unknown avg `223.8637` n `1212`
- 4h: commodity avg `-0.0073` n `13`; crypto_alt avg `-0.1414` n `239`; crypto_major avg `-0.1778` n `8`; equity avg `0.0304` n `166`; fx avg `0.0105` n `6`; index avg `-0.0859` n `27`; metal avg `0.0142` n `20`; unknown avg `494.8589` n `1200`
- 24h: commodity avg `0.4548` n `13`; crypto_alt avg `0.3975` n `239`; crypto_major avg `1.1954` n `8`; equity avg `0.1438` n `166`; fx avg `-0.1186` n `6`; index avg `-0.0734` n `27`; metal avg `0.1747` n `20`; unknown avg `413.2069` n `1094`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
