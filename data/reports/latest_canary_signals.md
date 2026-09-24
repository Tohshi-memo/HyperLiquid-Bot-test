# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T01:07:27.907118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0404` n `12`; crypto_alt avg `0.2383` n `234`; crypto_major avg `0.199` n `8`; equity avg `0.132` n `141`; fx avg `-0.0621` n `6`; index avg `0.0224` n `26`; metal avg `0.0659` n `20`; unknown avg `0.133` n `943`
- 1h: commodity avg `-0.112` n `12`; crypto_alt avg `-0.1544` n `234`; crypto_major avg `-0.1131` n `8`; equity avg `-0.0456` n `141`; fx avg `0.0194` n `6`; index avg `0.0157` n `26`; metal avg `0.0457` n `20`; unknown avg `-0.0778` n `943`
- 4h: commodity avg `-0.2473` n `12`; crypto_alt avg `0.5709` n `234`; crypto_major avg `0.6481` n `8`; equity avg `-0.0574` n `141`; fx avg `0.0221` n `6`; index avg `-0.0202` n `26`; metal avg `0.008` n `20`; unknown avg `-0.4716` n `921`
- 24h: commodity avg `0.2859` n `12`; crypto_alt avg `-4.5516` n `234`; crypto_major avg `-3.7438` n `8`; equity avg `-1.6586` n `140`; fx avg `0.0462` n `6`; index avg `-0.326` n `26`; metal avg `-0.7207` n `20`; unknown avg `583.0552` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
