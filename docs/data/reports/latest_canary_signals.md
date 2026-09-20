# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T15:22:30.437644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `-0.0509` n `234`; crypto_major avg `-0.0763` n `8`; equity avg `0.0101` n `140`; fx avg `-0.0389` n `6`; index avg `-0.0036` n `26`; metal avg `0.0017` n `20`; unknown avg `0.1828` n `943`
- 1h: commodity avg `-0.0035` n `12`; crypto_alt avg `0.5667` n `234`; crypto_major avg `0.4355` n `8`; equity avg `0.0728` n `140`; fx avg `-0.0098` n `6`; index avg `0.004` n `26`; metal avg `0.0015` n `20`; unknown avg `1.5503` n `941`
- 4h: commodity avg `0.0157` n `12`; crypto_alt avg `0.6311` n `234`; crypto_major avg `0.6484` n `8`; equity avg `0.0897` n `140`; fx avg `-0.0308` n `6`; index avg `0.0126` n `26`; metal avg `0.0046` n `20`; unknown avg `2.7717` n `935`
- 24h: commodity avg `0.3191` n `12`; crypto_alt avg `-1.8738` n `234`; crypto_major avg `-2.1178` n `8`; equity avg `-0.2413` n `140`; fx avg `-0.0563` n `6`; index avg `-0.055` n `26`; metal avg `-0.0347` n `20`; unknown avg `322.2511` n `819`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
