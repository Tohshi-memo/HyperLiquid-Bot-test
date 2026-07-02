# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T04:07:29.814942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.0651` n `228`; crypto_major avg `-0.2568` n `8`; equity avg `-0.016` n `88`; fx avg `-0.0235` n `6`; index avg `-0.0129` n `25`; metal avg `-0.0118` n `20`; unknown avg `0.6878` n `763`
- 1h: commodity avg `0.0041` n `12`; crypto_alt avg `0.4352` n `228`; crypto_major avg `0.4932` n `8`; equity avg `-0.1455` n `88`; fx avg `-0.0315` n `6`; index avg `-0.0646` n `25`; metal avg `0.1129` n `20`; unknown avg `0.2252` n `761`
- 4h: commodity avg `-0.0435` n `12`; crypto_alt avg `1.4245` n `228`; crypto_major avg `1.312` n `8`; equity avg `0.2702` n `88`; fx avg `-0.0345` n `6`; index avg `0.1235` n `25`; metal avg `0.5171` n `20`; unknown avg `0.5132` n `759`
- 24h: commodity avg `-0.6797` n `12`; crypto_alt avg `1.6994` n `228`; crypto_major avg `1.2106` n `8`; equity avg `-1.4456` n `88`; fx avg `-0.0534` n `6`; index avg `-0.3827` n `25`; metal avg `1.194` n `20`; unknown avg `25.4282` n `735`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
