# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T22:22:42.574417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `13`; crypto_alt avg `-0.1109` n `235`; crypto_major avg `-0.0204` n `8`; equity avg `0.0104` n `150`; fx avg `0.0014` n `6`; index avg `0.0003` n `26`; metal avg `-0.0041` n `20`; unknown avg `0.5301` n `1076`
- 1h: commodity avg `0.0552` n `13`; crypto_alt avg `0.0904` n `235`; crypto_major avg `0.0997` n `8`; equity avg `0.0558` n `150`; fx avg `-0.0019` n `6`; index avg `0.0104` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.3224` n `1058`
- 4h: commodity avg `0.329` n `13`; crypto_alt avg `-0.4235` n `235`; crypto_major avg `-0.1795` n `8`; equity avg `-0.0978` n `150`; fx avg `-0.0086` n `6`; index avg `-0.0242` n `26`; metal avg `-0.0136` n `20`; unknown avg `0.7193` n `990`
- 24h: commodity avg `0.3243` n `13`; crypto_alt avg `-1.6076` n `235`; crypto_major avg `-1.1771` n `8`; equity avg `0.3793` n `149`; fx avg `0.0734` n `6`; index avg `-0.0068` n `26`; metal avg `0.0128` n `20`; unknown avg `871.0219` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
