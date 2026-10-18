# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T00:59:43.468728+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `13`; crypto_alt avg `0.1346` n `237`; crypto_major avg `0.1563` n `8`; equity avg `0.2293` n `151`; fx avg `-0.0031` n `6`; index avg `0.0403` n `26`; metal avg `0.0099` n `20`; unknown avg `0.2002` n `1193`
- 1h: commodity avg `-0.0281` n `13`; crypto_alt avg `-0.0843` n `236`; crypto_major avg `0.1858` n `8`; equity avg `-0.0592` n `151`; fx avg `-0.0002` n `6`; index avg `0.0173` n `26`; metal avg `0.0079` n `20`; unknown avg `5.3429` n `1185`
- 4h: commodity avg `-0.0658` n `13`; crypto_alt avg `-1.0047` n `236`; crypto_major avg `-0.5672` n `8`; equity avg `-0.7182` n `151`; fx avg `0.0014` n `6`; index avg `-0.0661` n `26`; metal avg `-0.0304` n `20`; unknown avg `0.078` n `1179`
- 24h: commodity avg `-0.1464` n `13`; crypto_alt avg `-2.1507` n `236`; crypto_major avg `-0.6672` n `8`; equity avg `-0.7179` n `151`; fx avg `-0.0189` n `6`; index avg `-0.0736` n `26`; metal avg `-0.055` n `20`; unknown avg `5.2476` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1633`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1328`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0731`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
