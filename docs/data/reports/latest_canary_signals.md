# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T12:07:26.066130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1833` n `12`; crypto_alt avg `0.1713` n `228`; crypto_major avg `0.0015` n `8`; equity avg `-0.0105` n `78`; fx avg `0.0121` n `6`; index avg `0.0068` n `23`; metal avg `0.0017` n `18`; unknown avg `-0.0112` n `702`
- 1h: commodity avg `0.2343` n `12`; crypto_alt avg `-0.2349` n `228`; crypto_major avg `-0.3925` n `8`; equity avg `-0.0791` n `78`; fx avg `0.0158` n `6`; index avg `0.0008` n `23`; metal avg `0.0017` n `18`; unknown avg `-0.0813` n `702`
- 4h: commodity avg `0.1567` n `12`; crypto_alt avg `-0.0509` n `228`; crypto_major avg `-0.2897` n `8`; equity avg `-0.103` n `78`; fx avg `0.0134` n `6`; index avg `0.0006` n `23`; metal avg `-0.0634` n `18`; unknown avg `-0.2813` n `702`
- 24h: commodity avg `0.2854` n `12`; crypto_alt avg `1.192` n `228`; crypto_major avg `-0.5483` n `8`; equity avg `0.3083` n `78`; fx avg `0.031` n `6`; index avg `0.0379` n `23`; metal avg `-0.0747` n `18`; unknown avg `0.1119` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
