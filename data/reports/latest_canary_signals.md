# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T09:22:29.692798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0351` n `12`; crypto_alt avg `-0.2078` n `228`; crypto_major avg `-0.1975` n `8`; equity avg `-0.0407` n `74`; fx avg `-0.0035` n `6`; index avg `0.0083` n `23`; metal avg `-0.009` n `18`; unknown avg `-0.0644` n `645`
- 1h: commodity avg `0.1401` n `12`; crypto_alt avg `-0.3357` n `228`; crypto_major avg `-0.2358` n `8`; equity avg `-0.1137` n `74`; fx avg `-0.0143` n `6`; index avg `-0.0155` n `23`; metal avg `-0.0089` n `18`; unknown avg `-0.4786` n `645`
- 4h: commodity avg `-0.154` n `12`; crypto_alt avg `0.1231` n `228`; crypto_major avg `-0.2216` n `8`; equity avg `0.1328` n `74`; fx avg `-0.0202` n `6`; index avg `0.0311` n `23`; metal avg `0.0243` n `18`; unknown avg `1.7533` n `625`
- 24h: commodity avg `-1.5808` n `12`; crypto_alt avg `-0.0576` n `228`; crypto_major avg `0.4641` n `8`; equity avg `0.5657` n `74`; fx avg `-0.0036` n `6`; index avg `0.1768` n `23`; metal avg `0.0917` n `18`; unknown avg `-0.9509` n `599`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
