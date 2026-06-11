# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T00:52:28.111931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0211` n `12`; crypto_alt avg `0.1488` n `228`; crypto_major avg `0.1332` n `8`; equity avg `0.3197` n `74`; fx avg `0.004` n `6`; index avg `0.1501` n `23`; metal avg `0.3137` n `18`; unknown avg `-0.0359` n `550`
- 1h: commodity avg `-0.0786` n `12`; crypto_alt avg `0.6218` n `228`; crypto_major avg `0.405` n `8`; equity avg `0.7278` n `74`; fx avg `0.0414` n `6`; index avg `0.0462` n `23`; metal avg `0.7234` n `18`; unknown avg `0.1044` n `550`
- 4h: commodity avg `0.3253` n `12`; crypto_alt avg `0.5589` n `228`; crypto_major avg `0.2313` n `8`; equity avg `0.2578` n `74`; fx avg `0.0219` n `6`; index avg `0.1526` n `23`; metal avg `0.1925` n `18`; unknown avg `-0.1621` n `550`
- 24h: commodity avg `1.4281` n `12`; crypto_alt avg `-1.3452` n `228`; crypto_major avg `-1.5285` n `8`; equity avg `-1.6819` n `74`; fx avg `0.0728` n `6`; index avg `-1.4779` n `23`; metal avg `-1.5552` n `18`; unknown avg `-0.366` n `537`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
