# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T21:22:18.007212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0949` n `12`; crypto_alt avg `0.203` n `228`; crypto_major avg `0.0822` n `8`; equity avg `-0.0404` n `66`; fx avg `-0.0119` n `6`; index avg `0.0334` n `23`; metal avg `0.0176` n `18`; unknown avg `0.0569` n `383`
- 1h: commodity avg `-0.0447` n `12`; crypto_alt avg `0.2368` n `228`; crypto_major avg `0.1462` n `8`; equity avg `-0.0048` n `66`; fx avg `-0.0355` n `6`; index avg `-0.0163` n `23`; metal avg `-0.0063` n `18`; unknown avg `-0.0153` n `383`
- 4h: commodity avg `0.0922` n `12`; crypto_alt avg `-0.1693` n `228`; crypto_major avg `-0.3658` n `8`; equity avg `-0.7755` n `66`; fx avg `0.013` n `6`; index avg `-0.4468` n `23`; metal avg `-0.673` n `18`; unknown avg `1.1446` n `383`
- 24h: commodity avg `1.0947` n `12`; crypto_alt avg `-0.0785` n `228`; crypto_major avg `-0.2127` n `8`; equity avg `-0.0144` n `66`; fx avg `0.0639` n `6`; index avg `-0.5997` n `23`; metal avg `-2.7328` n `18`; unknown avg `0.5779` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
