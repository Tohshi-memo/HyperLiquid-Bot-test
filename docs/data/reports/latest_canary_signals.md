# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T12:00:28.808942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2353` n `12`; crypto_alt avg `0.1247` n `228`; crypto_major avg `0.0087` n `8`; equity avg `-0.0067` n `78`; fx avg `0.0202` n `6`; index avg `0.012` n `23`; metal avg `-0.0042` n `18`; unknown avg `0.0327` n `702`
- 1h: commodity avg `0.2864` n `12`; crypto_alt avg `-0.2821` n `228`; crypto_major avg `-0.3854` n `8`; equity avg `-0.0753` n `78`; fx avg `0.0238` n `6`; index avg `0.0061` n `23`; metal avg `-0.0042` n `18`; unknown avg `-0.0387` n `702`
- 4h: commodity avg `0.2085` n `12`; crypto_alt avg `-0.0992` n `228`; crypto_major avg `-0.2826` n `8`; equity avg `-0.0992` n `78`; fx avg `0.0214` n `6`; index avg `0.0058` n `23`; metal avg `-0.0692` n `18`; unknown avg `-0.2595` n `702`
- 24h: commodity avg `0.3376` n `12`; crypto_alt avg `1.1359` n `228`; crypto_major avg `-0.5415` n `8`; equity avg `0.3122` n `78`; fx avg `0.039` n `6`; index avg `0.0432` n `23`; metal avg `-0.0805` n `18`; unknown avg `0.1168` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
