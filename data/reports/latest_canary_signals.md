# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T09:22:28.855271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `12`; crypto_alt avg `0.0319` n `228`; crypto_major avg `0.137` n `8`; equity avg `0.0212` n `78`; fx avg `-0.0066` n `6`; index avg `0.0012` n `23`; metal avg `0.0072` n `18`; unknown avg `-0.0049` n `702`
- 1h: commodity avg `0.0215` n `12`; crypto_alt avg `0.0822` n `228`; crypto_major avg `0.0069` n `8`; equity avg `-0.0263` n `78`; fx avg `-0.002` n `6`; index avg `0.0011` n `23`; metal avg `-0.0034` n `18`; unknown avg `0.0022` n `702`
- 4h: commodity avg `-0.0537` n `12`; crypto_alt avg `0.3402` n `228`; crypto_major avg `-0.3256` n `8`; equity avg `0.0055` n `78`; fx avg `-0.0095` n `6`; index avg `0.0016` n `23`; metal avg `0.0259` n `18`; unknown avg `-0.1268` n `662`
- 24h: commodity avg `0.0823` n `12`; crypto_alt avg `1.0263` n `228`; crypto_major avg `-0.074` n `8`; equity avg `0.2807` n `78`; fx avg `0.3257` n `6`; index avg `0.0201` n `23`; metal avg `-0.0222` n `18`; unknown avg `0.0145` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
