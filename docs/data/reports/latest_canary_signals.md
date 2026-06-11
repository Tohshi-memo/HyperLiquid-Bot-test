# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T15:22:38.682030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0812` n `12`; crypto_alt avg `0.2291` n `228`; crypto_major avg `0.2609` n `8`; equity avg `0.3092` n `74`; fx avg `-0.0029` n `6`; index avg `0.1981` n `23`; metal avg `0.0121` n `18`; unknown avg `0.4364` n `556`
- 1h: commodity avg `-0.1205` n `12`; crypto_alt avg `0.1652` n `228`; crypto_major avg `0.2748` n `8`; equity avg `0.2384` n `74`; fx avg `-0.0367` n `6`; index avg `0.1016` n `23`; metal avg `0.1961` n `18`; unknown avg `0.5499` n `556`
- 4h: commodity avg `0.1` n `12`; crypto_alt avg `-0.0275` n `228`; crypto_major avg `-0.1724` n `8`; equity avg `0.035` n `74`; fx avg `-0.0699` n `6`; index avg `0.1076` n `23`; metal avg `0.3874` n `18`; unknown avg `0.7705` n `556`
- 24h: commodity avg `-0.3127` n `12`; crypto_alt avg `0.2462` n `228`; crypto_major avg `0.1593` n `8`; equity avg `-0.0412` n `74`; fx avg `-0.0407` n `6`; index avg `0.1002` n `23`; metal avg `-0.5323` n `18`; unknown avg `3.0085` n `528`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
