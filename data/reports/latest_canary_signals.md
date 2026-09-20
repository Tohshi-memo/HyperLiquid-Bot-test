# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T18:07:30.093247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `-0.014` n `234`; crypto_major avg `-0.1111` n `8`; equity avg `-0.0236` n `140`; fx avg `-0.0012` n `6`; index avg `-0.003` n `26`; metal avg `-0.0177` n `20`; unknown avg `32.6388` n `941`
- 1h: commodity avg `0.0233` n `12`; crypto_alt avg `-0.0134` n `234`; crypto_major avg `-0.2608` n `8`; equity avg `-0.0247` n `140`; fx avg `-0.0076` n `6`; index avg `-0.0055` n `26`; metal avg `-0.011` n `20`; unknown avg `16.9461` n `929`
- 4h: commodity avg `0.0119` n `12`; crypto_alt avg `2.4596` n `234`; crypto_major avg `1.2636` n `8`; equity avg `0.2499` n `140`; fx avg `0.011` n `6`; index avg `0.0353` n `26`; metal avg `0.0041` n `20`; unknown avg `0.5884` n `879`
- 24h: commodity avg `0.3699` n `12`; crypto_alt avg `0.1278` n `234`; crypto_major avg `-0.913` n `8`; equity avg `-0.0409` n `140`; fx avg `-0.0374` n `6`; index avg `-0.0411` n `26`; metal avg `-0.0196` n `20`; unknown avg `72.4891` n `827`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
