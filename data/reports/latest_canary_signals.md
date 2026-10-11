# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T14:07:28.812735+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0143` n `13`; crypto_alt avg `-0.1345` n `235`; crypto_major avg `0.0036` n `8`; equity avg `-0.0115` n `150`; fx avg `-0.0016` n `6`; index avg `-0.0028` n `26`; metal avg `0.0056` n `20`; unknown avg `0.0344` n `1132`
- 1h: commodity avg `-0.0327` n `13`; crypto_alt avg `0.0108` n `235`; crypto_major avg `0.0525` n `8`; equity avg `-0.0065` n `150`; fx avg `-0.0267` n `6`; index avg `-0.0018` n `26`; metal avg `0.0028` n `20`; unknown avg `0.4418` n `1132`
- 4h: commodity avg `-0.0688` n `13`; crypto_alt avg `0.0732` n `235`; crypto_major avg `0.0623` n `8`; equity avg `0.0653` n `150`; fx avg `-0.0101` n `6`; index avg `0.005` n `26`; metal avg `0.0089` n `20`; unknown avg `0.3891` n `1053`
- 24h: commodity avg `0.2882` n `13`; crypto_alt avg `1.07` n `235`; crypto_major avg `-0.0195` n `8`; equity avg `0.1396` n `150`; fx avg `0.0032` n `6`; index avg `0.0125` n `26`; metal avg `0.01` n `20`; unknown avg `0.8127` n `941`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
