# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T11:07:32.626291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.053` n `13`; crypto_alt avg `0.2953` n `239`; crypto_major avg `0.2736` n `8`; equity avg `0.1768` n `157`; fx avg `0.0042` n `6`; index avg `0.0037` n `27`; metal avg `0.0047` n `20`; unknown avg `-0.141` n `1242`
- 1h: commodity avg `0.1952` n `13`; crypto_alt avg `0.4392` n `239`; crypto_major avg `0.2717` n `8`; equity avg `0.0574` n `157`; fx avg `0.0056` n `6`; index avg `-0.0073` n `27`; metal avg `-0.01` n `20`; unknown avg `-0.0188` n `1238`
- 4h: commodity avg `0.0343` n `13`; crypto_alt avg `1.2299` n `239`; crypto_major avg `0.9599` n `8`; equity avg `1.451` n `157`; fx avg `0.0721` n `6`; index avg `0.1508` n `27`; metal avg `-0.0548` n `20`; unknown avg `1.111` n `1212`
- 24h: commodity avg `-0.2435` n `13`; crypto_alt avg `-1.2883` n `238`; crypto_major avg `-0.6679` n `8`; equity avg `-3.3385` n `157`; fx avg `0.0249` n `6`; index avg `-0.2255` n `27`; metal avg `-0.475` n `20`; unknown avg `4.1397` n `1021`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
