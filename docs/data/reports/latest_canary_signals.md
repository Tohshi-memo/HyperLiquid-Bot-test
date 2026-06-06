# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T03:37:22.234661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1473` n `12`; crypto_alt avg `-0.2422` n `228`; crypto_major avg `-0.1278` n `8`; equity avg `0.0785` n `74`; fx avg `0.0029` n `6`; index avg `-0.1235` n `23`; metal avg `0.0191` n `18`; unknown avg `-0.2953` n `425`
- 1h: commodity avg `-0.1296` n `12`; crypto_alt avg `-0.9082` n `228`; crypto_major avg `-0.5957` n `8`; equity avg `0.0187` n `74`; fx avg `-0.0163` n `6`; index avg `-0.2003` n `23`; metal avg `0.0948` n `18`; unknown avg `-0.6684` n `425`
- 4h: commodity avg `0.2816` n `12`; crypto_alt avg `-0.7127` n `228`; crypto_major avg `-0.0988` n `8`; equity avg `-1.1676` n `74`; fx avg `-0.0436` n `6`; index avg `-0.5944` n `23`; metal avg `-0.3491` n `18`; unknown avg `-0.0482` n `425`
- 24h: commodity avg `-1.2161` n `12`; crypto_alt avg `-5.8409` n `228`; crypto_major avg `-5.0012` n `8`; equity avg `-6.6939` n `74`; fx avg `-0.2269` n `6`; index avg `-4.189` n `23`; metal avg `-4.0676` n `18`; unknown avg `-0.9515` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
