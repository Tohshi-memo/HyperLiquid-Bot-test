# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T07:07:31.813768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `-0.263` n `234`; crypto_major avg `-0.24` n `8`; equity avg `-0.1363` n `140`; fx avg `0.0463` n `6`; index avg `-0.0236` n `26`; metal avg `-0.0814` n `20`; unknown avg `-0.0414` n `943`
- 1h: commodity avg `0.0278` n `12`; crypto_alt avg `0.0773` n `234`; crypto_major avg `-0.0031` n `8`; equity avg `-0.0534` n `140`; fx avg `0.1095` n `6`; index avg `0.0001` n `26`; metal avg `-0.0899` n `20`; unknown avg `-0.0537` n `943`
- 4h: commodity avg `-0.0564` n `12`; crypto_alt avg `0.5769` n `234`; crypto_major avg `0.1336` n `8`; equity avg `0.0745` n `140`; fx avg `0.1301` n `6`; index avg `0.0395` n `26`; metal avg `-0.1166` n `20`; unknown avg `0.4521` n `921`
- 24h: commodity avg `-0.1535` n `12`; crypto_alt avg `3.902` n `234`; crypto_major avg `1.9051` n `8`; equity avg `1.3315` n `140`; fx avg `-0.0626` n `6`; index avg `0.1605` n `26`; metal avg `0.1279` n `20`; unknown avg `1.8525` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
