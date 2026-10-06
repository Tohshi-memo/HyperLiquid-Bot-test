# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T19:52:57.841960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0116` n `13`; crypto_alt avg `0.0939` n `235`; crypto_major avg `0.1229` n `8`; equity avg `0.0182` n `150`; fx avg `-0.0035` n `6`; index avg `-0.0058` n `26`; metal avg `-0.0081` n `20`; unknown avg `12.052` n `1076`
- 1h: commodity avg `0.0556` n `13`; crypto_alt avg `-0.4528` n `235`; crypto_major avg `-0.1937` n `8`; equity avg `-0.2495` n `150`; fx avg `-0.0025` n `6`; index avg `-0.0536` n `26`; metal avg `-0.0412` n `20`; unknown avg `50.8206` n `1074`
- 4h: commodity avg `0.4809` n `13`; crypto_alt avg `-0.9815` n `235`; crypto_major avg `-0.6505` n `8`; equity avg `-0.5383` n `150`; fx avg `-0.0086` n `6`; index avg `-0.1413` n `26`; metal avg `0.0231` n `20`; unknown avg `3.2926` n `1068`
- 24h: commodity avg `0.3202` n `13`; crypto_alt avg `-0.7553` n `235`; crypto_major avg `-0.5904` n `8`; equity avg `0.3395` n `149`; fx avg `0.0919` n `6`; index avg `-0.0148` n `26`; metal avg `0.0496` n `20`; unknown avg `382.4442` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
