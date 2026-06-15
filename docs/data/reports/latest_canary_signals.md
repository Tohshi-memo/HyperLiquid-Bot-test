# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T06:52:35.503550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.81` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `0.0235` n `228`; crypto_major avg `0.1968` n `8`; equity avg `0.1085` n `74`; fx avg `-0.0166` n `6`; index avg `0.2246` n `23`; metal avg `-0.0382` n `18`; unknown avg `0.205` n `689`
- 1h: commodity avg `-0.065` n `12`; crypto_alt avg `0.1085` n `228`; crypto_major avg `0.1867` n `8`; equity avg `0.1499` n `74`; fx avg `0.0205` n `6`; index avg `0.0755` n `23`; metal avg `-0.0295` n `18`; unknown avg `-0.1476` n `657`
- 4h: commodity avg `0.2797` n `12`; crypto_alt avg `0.4773` n `228`; crypto_major avg `0.2706` n `8`; equity avg `0.1239` n `74`; fx avg `0.0273` n `6`; index avg `0.1657` n `23`; metal avg `-0.6038` n `18`; unknown avg `0.0755` n `529`
- 24h: commodity avg `-0.8656` n `12`; crypto_alt avg `3.1283` n `228`; crypto_major avg `3.0854` n `8`; equity avg `1.832` n `74`; fx avg `0.0462` n `6`; index avg `0.9477` n `23`; metal avg `1.6409` n `18`; unknown avg `1.7532` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
