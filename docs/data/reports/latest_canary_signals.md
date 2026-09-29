# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T11:23:08.406351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0` n `12`; crypto_alt avg `-0.0148` n `234`; crypto_major avg `-0.1085` n `8`; equity avg `-0.0344` n `141`; fx avg `0.0061` n `6`; index avg `-0.0207` n `26`; metal avg `0.049` n `20`; unknown avg `211.6809` n `963`
- 1h: commodity avg `-0.0461` n `12`; crypto_alt avg `0.1819` n `234`; crypto_major avg `-0.0557` n `8`; equity avg `0.1693` n `141`; fx avg `-0.0162` n `6`; index avg `0.0404` n `26`; metal avg `0.0889` n `20`; unknown avg `0.2984` n `961`
- 4h: commodity avg `-0.4532` n `12`; crypto_alt avg `0.7593` n `234`; crypto_major avg `0.0308` n `8`; equity avg `0.4188` n `141`; fx avg `-0.0548` n `6`; index avg `0.0574` n `26`; metal avg `0.1384` n `20`; unknown avg `170.413` n `945`
- 24h: commodity avg `-0.6995` n `12`; crypto_alt avg `1.5117` n `234`; crypto_major avg `0.6833` n `8`; equity avg `-0.0461` n `141`; fx avg `-0.0909` n `6`; index avg `0.0073` n `26`; metal avg `-0.1009` n `20`; unknown avg `59.3508` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
