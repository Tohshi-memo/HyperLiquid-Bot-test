# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T17:07:25.488257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.271` n `12`; crypto_alt avg `-0.024` n `228`; crypto_major avg `-0.0123` n `8`; equity avg `0.151` n `67`; fx avg `-0.0017` n `6`; index avg `-0.0122` n `23`; metal avg `-0.0563` n `18`; unknown avg `0.0116` n `419`
- 1h: commodity avg `-0.4348` n `12`; crypto_alt avg `1.2265` n `228`; crypto_major avg `1.1702` n `8`; equity avg `0.308` n `67`; fx avg `-0.0117` n `6`; index avg `0.2984` n `23`; metal avg `0.4905` n `18`; unknown avg `0.3019` n `419`
- 4h: commodity avg `0.2202` n `12`; crypto_alt avg `0.9971` n `228`; crypto_major avg `1.3929` n `8`; equity avg `1.8054` n `67`; fx avg `-0.0362` n `6`; index avg `1.1879` n `23`; metal avg `1.4216` n `18`; unknown avg `0.0206` n `419`
- 24h: commodity avg `0.3259` n `12`; crypto_alt avg `-4.1074` n `228`; crypto_major avg `-1.6712` n `8`; equity avg `1.5645` n `67`; fx avg `-0.029` n `6`; index avg `1.2509` n `23`; metal avg `0.7562` n `18`; unknown avg `-1.0959` n `408`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1883`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
