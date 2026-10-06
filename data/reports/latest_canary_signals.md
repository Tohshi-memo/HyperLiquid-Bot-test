# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T10:22:28.252837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `13`; crypto_alt avg `0.31` n `235`; crypto_major avg `0.1904` n `8`; equity avg `0.0937` n `150`; fx avg `-0.0059` n `6`; index avg `0.0186` n `26`; metal avg `-0.008` n `20`; unknown avg `-0.0` n `1074`
- 1h: commodity avg `-0.1194` n `13`; crypto_alt avg `0.2993` n `235`; crypto_major avg `-0.0367` n `8`; equity avg `0.1254` n `150`; fx avg `0.0163` n `6`; index avg `0.0148` n `26`; metal avg `-0.0534` n `20`; unknown avg `0.0134` n `1072`
- 4h: commodity avg `-0.3079` n `13`; crypto_alt avg `1.0213` n `235`; crypto_major avg `0.6868` n `8`; equity avg `0.2465` n `149`; fx avg `0.0399` n `6`; index avg `0.0338` n `26`; metal avg `0.0478` n `20`; unknown avg `-0.0496` n `992`
- 24h: commodity avg `-0.7406` n `13`; crypto_alt avg `-0.541` n `235`; crypto_major avg `-0.2981` n `8`; equity avg `0.608` n `149`; fx avg `0.0326` n `6`; index avg `0.236` n `26`; metal avg `-0.1231` n `20`; unknown avg `0.1505` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
