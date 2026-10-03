# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T08:07:32.328921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0207` n `13`; crypto_alt avg `-0.1104` n `235`; crypto_major avg `-0.0145` n `8`; equity avg `0.0253` n `143`; fx avg `0.0025` n `6`; index avg `-0.0011` n `26`; metal avg `0.0093` n `20`; unknown avg `-0.0296` n `966`
- 1h: commodity avg `0.0059` n `13`; crypto_alt avg `-0.4325` n `235`; crypto_major avg `-0.0117` n `8`; equity avg `0.0081` n `143`; fx avg `-0.0002` n `6`; index avg `-0.0028` n `26`; metal avg `0.0032` n `20`; unknown avg `0.091` n `966`
- 4h: commodity avg `-0.0079` n `13`; crypto_alt avg `-0.604` n `235`; crypto_major avg `-0.2027` n `8`; equity avg `-0.0063` n `143`; fx avg `-0.0037` n `6`; index avg `-0.0142` n `26`; metal avg `0.0058` n `20`; unknown avg `0.1357` n `944`
- 24h: commodity avg `0.6444` n `13`; crypto_alt avg `-2.3514` n `235`; crypto_major avg `-2.1594` n `8`; equity avg `0.0836` n `142`; fx avg `0.0207` n `6`; index avg `0.134` n `26`; metal avg `-0.3917` n `20`; unknown avg `-0.4488` n `862`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
