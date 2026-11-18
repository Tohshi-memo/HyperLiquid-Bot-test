# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T07:22:43.381232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0369` n `13`; crypto_alt avg `0.0022` n `239`; crypto_major avg `0.116` n `8`; equity avg `0.1247` n `163`; fx avg `-0.0001` n `6`; index avg `0.0041` n `27`; metal avg `-0.0325` n `20`; unknown avg `0.4744` n `1264`
- 1h: commodity avg `-0.1384` n `13`; crypto_alt avg `0.1232` n `239`; crypto_major avg `0.185` n `8`; equity avg `0.2996` n `163`; fx avg `-0.0334` n `6`; index avg `0.0051` n `27`; metal avg `-0.0865` n `20`; unknown avg `0.6037` n `1260`
- 4h: commodity avg `-0.3331` n `13`; crypto_alt avg `0.6377` n `239`; crypto_major avg `0.7174` n `8`; equity avg `0.8455` n `163`; fx avg `-0.038` n `6`; index avg `0.1039` n `27`; metal avg `-0.1089` n `20`; unknown avg `5.0354` n `1224`
- 24h: commodity avg `-0.0838` n `13`; crypto_alt avg `0.4031` n `239`; crypto_major avg `0.7656` n `8`; equity avg `0.7579` n `163`; fx avg `-0.1177` n `6`; index avg `0.0504` n `27`; metal avg `-0.9669` n `20`; unknown avg `234.2211` n `1105`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
