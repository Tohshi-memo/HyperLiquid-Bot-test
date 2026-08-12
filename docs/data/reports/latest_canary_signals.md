# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T08:37:31.337562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `-0.0679` n `230`; crypto_major avg `-0.083` n `8`; equity avg `-0.0581` n `113`; fx avg `0.0033` n `6`; index avg `-0.0158` n `25`; metal avg `-0.0` n `20`; unknown avg `-0.0206` n `786`
- 1h: commodity avg `-0.0248` n `12`; crypto_alt avg `-0.0697` n `230`; crypto_major avg `-0.0105` n `8`; equity avg `0.2619` n `113`; fx avg `-0.0175` n `6`; index avg `0.0368` n `25`; metal avg `0.0445` n `20`; unknown avg `-0.0149` n `786`
- 4h: commodity avg `-0.0281` n `12`; crypto_alt avg `-0.524` n `230`; crypto_major avg `-0.0146` n `8`; equity avg `0.3921` n `113`; fx avg `0.018` n `6`; index avg `0.0483` n `25`; metal avg `0.1226` n `20`; unknown avg `-0.0579` n `770`
- 24h: commodity avg `-0.1169` n `12`; crypto_alt avg `-1.2367` n `230`; crypto_major avg `0.6762` n `8`; equity avg `2.6724` n `113`; fx avg `0.0015` n `6`; index avg `0.2577` n `25`; metal avg `0.1862` n `20`; unknown avg `-0.12` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2306`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2275`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2026`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1732`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
