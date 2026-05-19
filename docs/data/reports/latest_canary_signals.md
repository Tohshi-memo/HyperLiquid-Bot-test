# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T20:22:21.201578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0436` n `12`; crypto_alt avg `0.0374` n `228`; crypto_major avg `-0.0272` n `8`; equity avg `-0.0013` n `66`; fx avg `-0.0016` n `6`; index avg `-0.0713` n `23`; metal avg `0.0502` n `18`; unknown avg `-0.0512` n `383`
- 1h: commodity avg `-0.1131` n `12`; crypto_alt avg `0.0432` n `228`; crypto_major avg `0.0194` n `8`; equity avg `-0.1778` n `66`; fx avg `0.0324` n `6`; index avg `-0.2135` n `23`; metal avg `-0.1279` n `18`; unknown avg `0.0159` n `383`
- 4h: commodity avg `0.2931` n `12`; crypto_alt avg `0.3508` n `228`; crypto_major avg `0.1719` n `8`; equity avg `0.5631` n `66`; fx avg `0.086` n `6`; index avg `0.2488` n `23`; metal avg `-0.2871` n `18`; unknown avg `1.3809` n `383`
- 24h: commodity avg `1.4571` n `12`; crypto_alt avg `-0.219` n `228`; crypto_major avg `-0.1825` n `8`; equity avg `0.1462` n `66`; fx avg `0.0658` n `6`; index avg `-0.5243` n `23`; metal avg `-2.651` n `18`; unknown avg `0.8759` n `363`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
