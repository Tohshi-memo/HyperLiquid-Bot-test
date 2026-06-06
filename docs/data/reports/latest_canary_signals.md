# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T09:52:21.284325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0376` n `12`; crypto_alt avg `-1.0238` n `228`; crypto_major avg `-0.9675` n `8`; equity avg `-0.1754` n `74`; fx avg `0.006` n `6`; index avg `-0.2375` n `23`; metal avg `-0.0272` n `18`; unknown avg `0.8216` n `425`
- 1h: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.7724` n `228`; crypto_major avg `-1.0017` n `8`; equity avg `0.0389` n `74`; fx avg `0.0001` n `6`; index avg `-0.0119` n `23`; metal avg `-0.0222` n `18`; unknown avg `-0.1826` n `425`
- 4h: commodity avg `-0.1213` n `12`; crypto_alt avg `0.9593` n `228`; crypto_major avg `0.2742` n `8`; equity avg `-0.0926` n `74`; fx avg `-0.0066` n `6`; index avg `0.133` n `23`; metal avg `0.1823` n `18`; unknown avg `1.5365` n `415`
- 24h: commodity avg `-1.3064` n `12`; crypto_alt avg `-4.2616` n `228`; crypto_major avg `-3.8736` n `8`; equity avg `-6.9457` n `74`; fx avg `-0.2455` n `6`; index avg `-4.1442` n `23`; metal avg `-4.2935` n `18`; unknown avg `1.2116` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
