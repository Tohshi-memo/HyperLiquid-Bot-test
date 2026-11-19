# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T08:52:30.450267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `13`; crypto_alt avg `0.0767` n `239`; crypto_major avg `-0.0344` n `8`; equity avg `-0.1542` n `164`; fx avg `-0.0078` n `6`; index avg `-0.0201` n `27`; metal avg `-0.0188` n `20`; unknown avg `0.275` n `1266`
- 1h: commodity avg `-0.0225` n `13`; crypto_alt avg `0.1123` n `239`; crypto_major avg `-0.0613` n `8`; equity avg `0.0825` n `164`; fx avg `0.016` n `6`; index avg `0.0167` n `27`; metal avg `0.025` n `20`; unknown avg `131.3838` n `1232`
- 4h: commodity avg `-0.0404` n `13`; crypto_alt avg `0.1774` n `239`; crypto_major avg `0.2586` n `8`; equity avg `1.1309` n `164`; fx avg `0.0571` n `6`; index avg `0.1846` n `27`; metal avg `0.0827` n `20`; unknown avg `100.1087` n `1202`
- 24h: commodity avg `0.2826` n `13`; crypto_alt avg `0.0225` n `239`; crypto_major avg `-0.79` n `8`; equity avg `0.1581` n `164`; fx avg `0.0558` n `6`; index avg `0.1574` n `27`; metal avg `-0.1341` n `20`; unknown avg `3.5636` n `1149`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
