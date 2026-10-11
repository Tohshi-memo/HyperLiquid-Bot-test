# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T18:22:34.827456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `13`; crypto_alt avg `-0.1313` n `235`; crypto_major avg `-0.1012` n `8`; equity avg `-0.0091` n `150`; fx avg `0.0014` n `6`; index avg `0.0049` n `26`; metal avg `-0.0065` n `20`; unknown avg `-0.006` n `1134`
- 1h: commodity avg `0.0259` n `13`; crypto_alt avg `-0.3058` n `235`; crypto_major avg `-0.2521` n `8`; equity avg `-0.0189` n `150`; fx avg `0.0027` n `6`; index avg `0.0056` n `26`; metal avg `-0.0184` n `20`; unknown avg `0.3271` n `1130`
- 4h: commodity avg `0.1483` n `13`; crypto_alt avg `1.5603` n `235`; crypto_major avg `1.2834` n `8`; equity avg `0.2485` n `150`; fx avg `0.0046` n `6`; index avg `0.0387` n `26`; metal avg `0.0386` n `20`; unknown avg `1.5777` n `1102`
- 24h: commodity avg `0.2755` n `13`; crypto_alt avg `1.9335` n `235`; crypto_major avg `0.9675` n `8`; equity avg `0.336` n `150`; fx avg `0.0187` n `6`; index avg `0.0473` n `26`; metal avg `0.0762` n `20`; unknown avg `0.5418` n `917`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
