# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T02:07:31.200836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0578` n `12`; crypto_alt avg `-0.1509` n `234`; crypto_major avg `-0.1511` n `8`; equity avg `-0.1165` n `140`; fx avg `0.0443` n `6`; index avg `-0.0093` n `26`; metal avg `-0.071` n `20`; unknown avg `0.3984` n `943`
- 1h: commodity avg `-0.0947` n `12`; crypto_alt avg `-0.7766` n `234`; crypto_major avg `-0.687` n `8`; equity avg `-0.2969` n `140`; fx avg `-0.0186` n `6`; index avg `-0.0456` n `26`; metal avg `-0.1627` n `20`; unknown avg `1.1192` n `943`
- 4h: commodity avg `0.002` n `12`; crypto_alt avg `0.5202` n `234`; crypto_major avg `0.2422` n `8`; equity avg `-0.3405` n `140`; fx avg `-0.0384` n `6`; index avg `-0.0944` n `26`; metal avg `-0.2558` n `20`; unknown avg `0.544` n `937`
- 24h: commodity avg `-0.0141` n `12`; crypto_alt avg `2.2916` n `234`; crypto_major avg `1.0507` n `8`; equity avg `0.2586` n `140`; fx avg `-0.1692` n `6`; index avg `-0.0138` n `26`; metal avg `0.0369` n `20`; unknown avg `1.0085` n `836`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
