# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T11:37:38.823188+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0663` n `12`; crypto_alt avg `-0.1341` n `228`; crypto_major avg `-0.0647` n `8`; equity avg `0.0182` n `67`; fx avg `0.0035` n `6`; index avg `0.0296` n `23`; metal avg `-0.0067` n `18`; unknown avg `0.8198` n `396`
- 1h: commodity avg `-0.0628` n `12`; crypto_alt avg `-0.2032` n `228`; crypto_major avg `-0.103` n `8`; equity avg `0.0495` n `67`; fx avg `0.0094` n `6`; index avg `0.0722` n `23`; metal avg `0.0367` n `18`; unknown avg `0.8084` n `396`
- 4h: commodity avg `-0.0064` n `12`; crypto_alt avg `-1.2581` n `228`; crypto_major avg `-0.8281` n `8`; equity avg `-0.1014` n `67`; fx avg `-0.0243` n `6`; index avg `-0.0425` n `23`; metal avg `-0.14` n `18`; unknown avg `-0.1355` n `386`
- 24h: commodity avg `-0.3776` n `12`; crypto_alt avg `-5.6762` n `228`; crypto_major avg `-3.9409` n `8`; equity avg `-1.5411` n `67`; fx avg `0.065` n `6`; index avg `-0.1014` n `23`; metal avg `-0.7336` n `18`; unknown avg `-1.4269` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
