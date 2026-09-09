# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T15:21:13.784056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `-0.6398` n `233`; crypto_major avg `-0.4817` n `8`; equity avg `-0.272` n `134`; fx avg `-0.0045` n `6`; index avg `-0.0398` n `26`; metal avg `-0.1097` n `20`; unknown avg `0.3838` n `797`
- 1h: commodity avg `0.0264` n `12`; crypto_alt avg `-1.1254` n `233`; crypto_major avg `-0.8802` n `8`; equity avg `-0.1988` n `134`; fx avg `0.0152` n `6`; index avg `-0.0785` n `26`; metal avg `-0.181` n `20`; unknown avg `0.6417` n `795`
- 4h: commodity avg `0.019` n `12`; crypto_alt avg `-0.9361` n `233`; crypto_major avg `-0.8522` n `8`; equity avg `0.0947` n `134`; fx avg `0.021` n `6`; index avg `-0.0222` n `26`; metal avg `0.1438` n `20`; unknown avg `10.5057` n `766`
- 24h: commodity avg `0.4311` n `12`; crypto_alt avg `-1.7515` n `232`; crypto_major avg `-0.4388` n `8`; equity avg `-0.6194` n `134`; fx avg `-0.1065` n `6`; index avg `-0.2419` n `26`; metal avg `0.1149` n `20`; unknown avg `9.3726` n `685`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
