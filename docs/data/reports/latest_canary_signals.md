# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T02:37:23.015239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0874` n `12`; crypto_alt avg `-0.1148` n `228`; crypto_major avg `-0.0295` n `8`; equity avg `-0.0603` n `74`; fx avg `-0.0014` n `6`; index avg `-0.0256` n `23`; metal avg `-0.3194` n `18`; unknown avg `0.2094` n `550`
- 1h: commodity avg `0.0838` n `12`; crypto_alt avg `-0.151` n `228`; crypto_major avg `-0.0509` n `8`; equity avg `-0.785` n `74`; fx avg `0.0043` n `6`; index avg `-0.239` n `23`; metal avg `-0.9091` n `18`; unknown avg `-0.0893` n `550`
- 4h: commodity avg `-0.1807` n `12`; crypto_alt avg `1.6982` n `228`; crypto_major avg `1.2305` n `8`; equity avg `0.4867` n `74`; fx avg `0.1628` n `6`; index avg `0.3401` n `23`; metal avg `0.3783` n `18`; unknown avg `0.467` n `550`
- 24h: commodity avg `1.403` n `12`; crypto_alt avg `-0.3413` n `228`; crypto_major avg `-0.3792` n `8`; equity avg `-1.3609` n `74`; fx avg `0.0957` n `6`; index avg `-1.2448` n `23`; metal avg `-0.9697` n `18`; unknown avg `0.1115` n `537`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1832`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
