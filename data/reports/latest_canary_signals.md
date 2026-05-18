# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T17:37:19.117044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.074` n `12`; crypto_alt avg `-0.0507` n `228`; crypto_major avg `0.0223` n `8`; equity avg `-0.0373` n `66`; fx avg `-0.0032` n `5`; index avg `-0.0766` n `23`; metal avg `-0.0653` n `18`; unknown avg `-0.0486` n `384`
- 1h: commodity avg `0.0796` n `12`; crypto_alt avg `0.1495` n `228`; crypto_major avg `0.2701` n `8`; equity avg `0.1527` n `66`; fx avg `-0.0406` n `5`; index avg `-0.0628` n `23`; metal avg `0.1488` n `18`; unknown avg `-0.231` n `384`
- 4h: commodity avg `1.3515` n `12`; crypto_alt avg `-0.1168` n `228`; crypto_major avg `-0.2352` n `8`; equity avg `-1.5904` n `66`; fx avg `-0.0169` n `5`; index avg `-0.7652` n `23`; metal avg `-0.3382` n `18`; unknown avg `-0.4283` n `383`
- 24h: commodity avg `1.1526` n `12`; crypto_alt avg `-1.9131` n `228`; crypto_major avg `-1.5787` n `8`; equity avg `-0.8922` n `66`; fx avg `0.0136` n `5`; index avg `-0.5122` n `23`; metal avg `0.6162` n `18`; unknown avg `-0.2309` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
