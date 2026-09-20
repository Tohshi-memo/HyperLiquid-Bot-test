# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T09:37:26.120846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `0.1246` n `234`; crypto_major avg `0.1601` n `8`; equity avg `0.0268` n `140`; fx avg `-0.0005` n `6`; index avg `0.0018` n `26`; metal avg `0.0007` n `20`; unknown avg `0.7028` n `943`
- 1h: commodity avg `-0.0304` n `12`; crypto_alt avg `0.2507` n `234`; crypto_major avg `0.2534` n `8`; equity avg `0.0057` n `140`; fx avg `-0.0012` n `6`; index avg `-0.0013` n `26`; metal avg `0.016` n `20`; unknown avg `2.0644` n `941`
- 4h: commodity avg `0.0326` n `12`; crypto_alt avg `-0.3065` n `234`; crypto_major avg `0.1461` n `8`; equity avg `-0.0058` n `140`; fx avg `0.009` n `6`; index avg `-0.0156` n `26`; metal avg `0.0287` n `20`; unknown avg `1.6801` n `905`
- 24h: commodity avg `0.2298` n `12`; crypto_alt avg `-0.9328` n `234`; crypto_major avg `-1.5253` n `8`; equity avg `-0.2095` n `140`; fx avg `-0.0743` n `6`; index avg `-0.0679` n `26`; metal avg `0.0326` n `20`; unknown avg `1.1345` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
