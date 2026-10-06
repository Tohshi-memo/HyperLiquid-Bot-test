# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T03:37:23.977901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `13`; crypto_alt avg `-0.264` n `235`; crypto_major avg `-0.1705` n `8`; equity avg `-0.0026` n `149`; fx avg `-0.0012` n `6`; index avg `0.0103` n `26`; metal avg `-0.0172` n `20`; unknown avg `-0.0305` n `1074`
- 1h: commodity avg `0.0002` n `13`; crypto_alt avg `-0.3641` n `235`; crypto_major avg `-0.2661` n `8`; equity avg `0.0758` n `149`; fx avg `0.0004` n `6`; index avg `0.0158` n `26`; metal avg `0.021` n `20`; unknown avg `0.2838` n `1072`
- 4h: commodity avg `0.1012` n `13`; crypto_alt avg `-1.5148` n `235`; crypto_major avg `-0.6549` n `8`; equity avg `-0.1781` n `149`; fx avg `0.003` n `6`; index avg `-0.0534` n `26`; metal avg `-0.0701` n `20`; unknown avg `0.4326` n `1066`
- 24h: commodity avg `0.022` n `13`; crypto_alt avg `-1.2539` n `235`; crypto_major avg `-0.5992` n `8`; equity avg `-0.0118` n `149`; fx avg `0.0499` n `6`; index avg `0.0934` n `26`; metal avg `-0.0259` n `20`; unknown avg `611.7353` n `818`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1932`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
