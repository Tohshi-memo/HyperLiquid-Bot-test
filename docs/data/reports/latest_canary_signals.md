# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T00:22:29.228783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0613` n `12`; crypto_alt avg `0.5808` n `234`; crypto_major avg `0.5748` n `8`; equity avg `-0.0566` n `140`; fx avg `-0.0071` n `6`; index avg `-0.0288` n `26`; metal avg `-0.0812` n `20`; unknown avg `-0.2587` n `943`
- 1h: commodity avg `-0.1158` n `12`; crypto_alt avg `1.1327` n `234`; crypto_major avg `1.146` n `8`; equity avg `0.1643` n `140`; fx avg `-0.0262` n `6`; index avg `0.0148` n `26`; metal avg `-0.0665` n `20`; unknown avg `16.0926` n `935`
- 4h: commodity avg `-0.4227` n `12`; crypto_alt avg `1.2101` n `234`; crypto_major avg `1.4365` n `8`; equity avg `0.6444` n `140`; fx avg `0.0352` n `6`; index avg `0.1327` n `26`; metal avg `-0.0141` n `20`; unknown avg `3.4119` n `853`
- 24h: commodity avg `-0.2007` n `12`; crypto_alt avg `1.8333` n `234`; crypto_major avg `1.6023` n `8`; equity avg `0.5325` n `140`; fx avg `0.0331` n `6`; index avg `0.0806` n `26`; metal avg `-0.0582` n `20`; unknown avg `3.6979` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
