# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T21:22:44.690294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0328` n `12`; crypto_alt avg `-0.0388` n `228`; crypto_major avg `0.1958` n `8`; equity avg `0.0074` n `74`; fx avg `0.0074` n `6`; index avg `0.0101` n `23`; metal avg `-0.008` n `18`; unknown avg `-0.0301` n `550`
- 1h: commodity avg `0.3302` n `12`; crypto_alt avg `-0.975` n `228`; crypto_major avg `-0.45` n `8`; equity avg `-0.3581` n `74`; fx avg `-0.0218` n `6`; index avg `-0.0461` n `23`; metal avg `-0.1006` n `18`; unknown avg `-0.0932` n `550`
- 4h: commodity avg `0.0609` n `12`; crypto_alt avg `-2.1026` n `228`; crypto_major avg `-1.317` n `8`; equity avg `-1.2347` n `74`; fx avg `-0.0604` n `6`; index avg `-0.6101` n `23`; metal avg `-1.048` n `18`; unknown avg `-0.4116` n `549`
- 24h: commodity avg `1.4155` n `12`; crypto_alt avg `-2.8467` n `228`; crypto_major avg `-2.7658` n `8`; equity avg `-2.2286` n `74`; fx avg `-0.0795` n `6`; index avg `-1.6535` n `23`; metal avg `-2.6597` n `18`; unknown avg `-0.5454` n `537`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
