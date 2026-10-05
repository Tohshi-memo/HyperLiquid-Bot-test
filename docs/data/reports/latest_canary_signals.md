# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T01:07:32.262539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.5` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0121` n `13`; crypto_alt avg `0.0371` n `235`; crypto_major avg `-0.1483` n `8`; equity avg `0.0708` n `144`; fx avg `-0.0671` n `6`; index avg `0.0116` n `26`; metal avg `0.0843` n `20`; unknown avg `0.1609` n `1072`
- 1h: commodity avg `0.0514` n `13`; crypto_alt avg `0.3111` n `235`; crypto_major avg `0.0525` n `8`; equity avg `0.1825` n `144`; fx avg `-0.051` n `6`; index avg `0.0331` n `26`; metal avg `0.1905` n `20`; unknown avg `0.8135` n `1068`
- 4h: commodity avg `-0.2119` n `13`; crypto_alt avg `0.7262` n `235`; crypto_major avg `0.2806` n `8`; equity avg `0.4254` n `144`; fx avg `-0.0552` n `6`; index avg `0.0409` n `26`; metal avg `0.2663` n `20`; unknown avg `1.1316` n `996`
- 24h: commodity avg `-0.2405` n `13`; crypto_alt avg `1.4069` n `235`; crypto_major avg `1.5049` n `8`; equity avg `0.6219` n `144`; fx avg `-0.0472` n `6`; index avg `0.04` n `26`; metal avg `0.2782` n `20`; unknown avg `0.7775` n `950`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.196`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1813`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
