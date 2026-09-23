# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T03:22:26.349939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `0.4959` n `234`; crypto_major avg `0.4308` n `8`; equity avg `-0.0238` n `140`; fx avg `-0.0016` n `6`; index avg `-0.0033` n `26`; metal avg `0.0173` n `20`; unknown avg `0.0205` n `945`
- 1h: commodity avg `-0.0248` n `12`; crypto_alt avg `0.8546` n `234`; crypto_major avg `0.5226` n `8`; equity avg `-0.0095` n `140`; fx avg `-0.0047` n `6`; index avg `0.001` n `26`; metal avg `-0.0065` n `20`; unknown avg `-0.2948` n `943`
- 4h: commodity avg `-0.0057` n `12`; crypto_alt avg `0.3092` n `234`; crypto_major avg `0.5527` n `8`; equity avg `-0.4074` n `140`; fx avg `-0.0686` n `6`; index avg `-0.1081` n `26`; metal avg `-0.2985` n `20`; unknown avg `-0.0503` n `937`
- 24h: commodity avg `-0.0805` n `12`; crypto_alt avg `4.3359` n `234`; crypto_major avg `2.6597` n `8`; equity avg `0.2853` n `140`; fx avg `-0.2019` n `6`; index avg `-0.0069` n `26`; metal avg `0.0879` n `20`; unknown avg `1.0948` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
