# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T01:07:30.396959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0227` n `12`; crypto_alt avg `0.3812` n `228`; crypto_major avg `0.1975` n `8`; equity avg `0.4821` n `74`; fx avg `0.0348` n `6`; index avg `0.2386` n `23`; metal avg `-0.0216` n `18`; unknown avg `0.1555` n `550`
- 1h: commodity avg `-0.0809` n `12`; crypto_alt avg `0.7575` n `228`; crypto_major avg `0.5074` n `8`; equity avg `1.2368` n `74`; fx avg `0.0506` n `6`; index avg `0.2634` n `23`; metal avg `0.7968` n `18`; unknown avg `0.3405` n `550`
- 4h: commodity avg `0.1935` n `12`; crypto_alt avg `1.5027` n `228`; crypto_major avg `0.7693` n `8`; equity avg `0.7861` n `74`; fx avg `0.089` n `6`; index avg `0.3297` n `23`; metal avg `0.1153` n `18`; unknown avg `0.024` n `550`
- 24h: commodity avg `1.6712` n `12`; crypto_alt avg `-1.23` n `228`; crypto_major avg `-1.4638` n `8`; equity avg `-1.4111` n `74`; fx avg `0.1133` n `6`; index avg `-1.2785` n `23`; metal avg `-1.0778` n `18`; unknown avg `-0.2878` n `537`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
