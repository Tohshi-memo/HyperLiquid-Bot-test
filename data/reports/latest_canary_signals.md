# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T00:07:29.397845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `13`; crypto_alt avg `0.4471` n `236`; crypto_major avg `0.0616` n `8`; equity avg `0.0351` n `151`; fx avg `0.0064` n `6`; index avg `-0.0242` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.0022` n `1128`
- 1h: commodity avg `-0.0085` n `13`; crypto_alt avg `0.4146` n `236`; crypto_major avg `0.0058` n `8`; equity avg `-0.3002` n `151`; fx avg `-0.003` n `6`; index avg `-0.0817` n `26`; metal avg `-0.0541` n `20`; unknown avg `-0.0931` n `1128`
- 4h: commodity avg `-0.102` n `13`; crypto_alt avg `0.1897` n `236`; crypto_major avg `-0.2877` n `8`; equity avg `-0.6086` n `151`; fx avg `-0.0116` n `6`; index avg `-0.1438` n `26`; metal avg `-0.0976` n `20`; unknown avg `-0.4738` n `1036`
- 24h: commodity avg `-0.2627` n `13`; crypto_alt avg `0.5899` n `236`; crypto_major avg `0.3249` n `8`; equity avg `0.8318` n `151`; fx avg `0.0846` n `6`; index avg `0.0141` n `26`; metal avg `0.3694` n `20`; unknown avg `24.6687` n `910`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0958`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0862`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0857`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.085`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0634`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0632`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0563`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
