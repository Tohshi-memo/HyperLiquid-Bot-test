# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T11:52:32.089350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `13`; crypto_alt avg `-0.0037` n `236`; crypto_major avg `-0.0691` n `8`; equity avg `-0.0228` n `151`; fx avg `0.0025` n `6`; index avg `-0.0095` n `26`; metal avg `0.0064` n `20`; unknown avg `0.0474` n `1193`
- 1h: commodity avg `0.0105` n `13`; crypto_alt avg `-0.2863` n `236`; crypto_major avg `-0.248` n `8`; equity avg `-0.058` n `151`; fx avg `0.0022` n `6`; index avg `0.0057` n `26`; metal avg `0.0095` n `20`; unknown avg `-0.0765` n `1191`
- 4h: commodity avg `0.0527` n `13`; crypto_alt avg `-0.3854` n `236`; crypto_major avg `-0.3317` n `8`; equity avg `0.0326` n `151`; fx avg `0.0049` n `6`; index avg `0.0223` n `26`; metal avg `0.0079` n `20`; unknown avg `-0.1695` n `1173`
- 24h: commodity avg `0.2479` n `13`; crypto_alt avg `-2.7338` n `236`; crypto_major avg `-1.962` n `8`; equity avg `-3.2072` n `151`; fx avg `-0.0007` n `6`; index avg `-0.505` n `26`; metal avg `-0.2184` n `20`; unknown avg `8.5256` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1858`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1501`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1246`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1173`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.072`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
