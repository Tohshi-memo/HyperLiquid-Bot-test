# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T17:22:31.549537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `0.141` n `233`; crypto_major avg `0.1169` n `8`; equity avg `-0.0106` n `134`; fx avg `0.0095` n `6`; index avg `0.0084` n `26`; metal avg `-0.0187` n `20`; unknown avg `12.81` n `797`
- 1h: commodity avg `-0.1805` n `12`; crypto_alt avg `0.9343` n `233`; crypto_major avg `0.5411` n `8`; equity avg `0.2365` n `134`; fx avg `0.0284` n `6`; index avg `0.0568` n `26`; metal avg `0.2276` n `20`; unknown avg `0.6226` n `789`
- 4h: commodity avg `-0.1674` n `12`; crypto_alt avg `-0.8507` n `233`; crypto_major avg `-1.0003` n `8`; equity avg `-0.0053` n `134`; fx avg `0.0567` n `6`; index avg `-0.0242` n `26`; metal avg `0.1726` n `20`; unknown avg `8.6052` n `767`
- 24h: commodity avg `0.3346` n `12`; crypto_alt avg `-0.6664` n `233`; crypto_major avg `-0.0712` n `8`; equity avg `-0.6795` n `134`; fx avg `-0.0616` n `6`; index avg `-0.2202` n `26`; metal avg `0.462` n `20`; unknown avg `7.6205` n `699`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
