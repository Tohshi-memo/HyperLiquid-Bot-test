# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T14:07:42.117082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `13`; crypto_alt avg `-0.3624` n `235`; crypto_major avg `-0.3157` n `8`; equity avg `0.1394` n `150`; fx avg `0.0138` n `6`; index avg `0.0431` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.6742` n `1072`
- 1h: commodity avg `0.1411` n `13`; crypto_alt avg `-0.3285` n `235`; crypto_major avg `0.0052` n `8`; equity avg `0.2786` n `150`; fx avg `-0.0189` n `6`; index avg `0.0156` n `26`; metal avg `-0.0941` n `20`; unknown avg `81.5418` n `1072`
- 4h: commodity avg `0.1217` n `13`; crypto_alt avg `0.035` n `235`; crypto_major avg `0.2081` n `8`; equity avg `0.6368` n `150`; fx avg `0.0338` n `6`; index avg `0.1193` n `26`; metal avg `-0.0514` n `20`; unknown avg `2.9232` n `1064`
- 24h: commodity avg `-0.4175` n `13`; crypto_alt avg `-0.7766` n `235`; crypto_major avg `-0.5783` n `8`; equity avg `1.2491` n `149`; fx avg `0.1273` n `6`; index avg `0.2602` n `26`; metal avg `-0.1138` n `20`; unknown avg `1.5353` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1732`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
