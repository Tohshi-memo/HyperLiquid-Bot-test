# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T07:22:27.878863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `13`; crypto_alt avg `-0.6721` n `239`; crypto_major avg `-0.5369` n `8`; equity avg `-0.0845` n `162`; fx avg `0.0056` n `6`; index avg `0.0017` n `27`; metal avg `-0.0046` n `20`; unknown avg `0.0522` n `1260`
- 1h: commodity avg `0.0327` n `13`; crypto_alt avg `-1.5021` n `239`; crypto_major avg `-0.8083` n `8`; equity avg `-0.1384` n `162`; fx avg `-0.0037` n `6`; index avg `-0.0108` n `27`; metal avg `0.0031` n `20`; unknown avg `11.8843` n `1252`
- 4h: commodity avg `0.0048` n `13`; crypto_alt avg `-1.315` n `239`; crypto_major avg `-0.8232` n `8`; equity avg `-0.0507` n `162`; fx avg `0.0047` n `6`; index avg `-0.0023` n `27`; metal avg `0.0006` n `20`; unknown avg `4.9229` n `1214`
- 24h: commodity avg `-0.1235` n `13`; crypto_alt avg `-3.4369` n `239`; crypto_major avg `-3.3976` n `8`; equity avg `-2.8148` n `162`; fx avg `-0.1389` n `6`; index avg `-0.2278` n `27`; metal avg `-0.4169` n `20`; unknown avg `64.5976` n `1018`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
