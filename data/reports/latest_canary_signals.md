# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T09:22:18.749199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.066` n `12`; crypto_alt avg `-0.0536` n `228`; crypto_major avg `0.0287` n `8`; equity avg `-0.0615` n `66`; fx avg `0.0086` n `5`; index avg `-0.0131` n `23`; metal avg `0.0034` n `18`; unknown avg `-0.0883` n `383`
- 1h: commodity avg `0.0504` n `12`; crypto_alt avg `0.0012` n `228`; crypto_major avg `0.0022` n `8`; equity avg `0.1551` n `66`; fx avg `0.0188` n `5`; index avg `0.0677` n `23`; metal avg `0.0553` n `18`; unknown avg `-0.1121` n `383`
- 4h: commodity avg `-0.1696` n `12`; crypto_alt avg `-0.7849` n `228`; crypto_major avg `-0.4966` n `8`; equity avg `0.8709` n `66`; fx avg `-0.0432` n `5`; index avg `0.3694` n `23`; metal avg `0.385` n `18`; unknown avg `-0.2909` n `363`
- 24h: commodity avg `0.7634` n `12`; crypto_alt avg `-2.9535` n `228`; crypto_major avg `-1.3693` n `8`; equity avg `0.5564` n `65`; fx avg `0.0495` n `5`; index avg `0.2936` n `23`; metal avg `0.1411` n `18`; unknown avg `-0.5086` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
