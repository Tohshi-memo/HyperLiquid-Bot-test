# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T07:22:32.725063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0744` n `12`; crypto_alt avg `0.3054` n `228`; crypto_major avg `0.1221` n `8`; equity avg `0.0665` n `74`; fx avg `0.0004` n `6`; index avg `0.0243` n `23`; metal avg `0.0324` n `18`; unknown avg `14.8638` n `643`
- 1h: commodity avg `-0.0526` n `12`; crypto_alt avg `0.8186` n `228`; crypto_major avg `0.382` n `8`; equity avg `0.1538` n `74`; fx avg `0.0005` n `6`; index avg `-0.0113` n `23`; metal avg `0.0691` n `18`; unknown avg `3.3981` n `643`
- 4h: commodity avg `0.0556` n `12`; crypto_alt avg `0.7153` n `228`; crypto_major avg `0.2447` n `8`; equity avg `-0.1477` n `74`; fx avg `0.0041` n `6`; index avg `0.0093` n `23`; metal avg `0.0227` n `18`; unknown avg `0.0182` n `619`
- 24h: commodity avg `-0.747` n `12`; crypto_alt avg `1.6446` n `228`; crypto_major avg `0.9756` n `8`; equity avg `0.3363` n `74`; fx avg `0.0144` n `6`; index avg `1.2587` n `23`; metal avg `1.1221` n `18`; unknown avg `36.8083` n `507`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
