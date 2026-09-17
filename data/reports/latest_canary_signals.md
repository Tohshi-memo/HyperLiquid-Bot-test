# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T16:07:27.403783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0527` n `12`; crypto_alt avg `0.1753` n `234`; crypto_major avg `-0.0915` n `8`; equity avg `-0.0207` n `138`; fx avg `-0.0073` n `6`; index avg `-0.0026` n `26`; metal avg `0.0085` n `20`; unknown avg `-0.0332` n `917`
- 1h: commodity avg `-0.0557` n `12`; crypto_alt avg `0.8329` n `234`; crypto_major avg `0.4916` n `8`; equity avg `0.2359` n `138`; fx avg `-0.0246` n `6`; index avg `0.0401` n `26`; metal avg `0.0807` n `20`; unknown avg `0.3528` n `915`
- 4h: commodity avg `0.1679` n `12`; crypto_alt avg `0.994` n `234`; crypto_major avg `0.9619` n `8`; equity avg `0.571` n `138`; fx avg `-0.0589` n `6`; index avg `0.0995` n `26`; metal avg `0.1787` n `20`; unknown avg `1.0547` n `891`
- 24h: commodity avg `-0.2201` n `12`; crypto_alt avg `5.171` n `234`; crypto_major avg `2.8071` n `8`; equity avg `1.7224` n `138`; fx avg `0.0163` n `6`; index avg `0.2312` n `26`; metal avg `0.2141` n `20`; unknown avg `0.5055` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
