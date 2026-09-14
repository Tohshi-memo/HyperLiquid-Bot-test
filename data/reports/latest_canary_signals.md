# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T03:52:28.622217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0305` n `12`; crypto_alt avg `-0.0672` n `233`; crypto_major avg `-0.1196` n `8`; equity avg `-0.0239` n `136`; fx avg `-0.0027` n `6`; index avg `-0.0104` n `27`; metal avg `-0.0066` n `20`; unknown avg `12.0501` n `888`
- 1h: commodity avg `0.0835` n `12`; crypto_alt avg `-0.104` n `233`; crypto_major avg `0.001` n `8`; equity avg `-0.1574` n `136`; fx avg `-0.0225` n `6`; index avg `-0.0493` n `27`; metal avg `-0.05` n `20`; unknown avg `9.1955` n `886`
- 4h: commodity avg `0.1131` n `12`; crypto_alt avg `1.485` n `233`; crypto_major avg `1.4909` n `8`; equity avg `0.2352` n `136`; fx avg `0.0162` n `6`; index avg `0.0248` n `27`; metal avg `0.0375` n `20`; unknown avg `29.9784` n `762`
- 24h: commodity avg `0.766` n `12`; crypto_alt avg `-0.4742` n `233`; crypto_major avg `-0.0544` n `8`; equity avg `-1.41` n `136`; fx avg `0.0522` n `6`; index avg `-0.322` n `26`; metal avg `-0.1503` n `20`; unknown avg `1.6022` n `676`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
