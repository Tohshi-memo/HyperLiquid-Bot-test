# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T20:06:05.239004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `-0.041` n `228`; crypto_major avg `-0.0068` n `8`; equity avg `-0.005` n `74`; fx avg `-0.012` n `6`; index avg `-0.0052` n `23`; metal avg `-0.0161` n `18`; unknown avg `0.8402` n `645`
- 1h: commodity avg `-0.0967` n `12`; crypto_alt avg `0.0811` n `228`; crypto_major avg `0.0496` n `8`; equity avg `-0.0079` n `74`; fx avg `0.0194` n `6`; index avg `0.0003` n `23`; metal avg `-0.0497` n `18`; unknown avg `1.3107` n `645`
- 4h: commodity avg `0.1598` n `12`; crypto_alt avg `-0.1089` n `228`; crypto_major avg `-0.1486` n `8`; equity avg `-0.0984` n `74`; fx avg `-0.0133` n `6`; index avg `-0.071` n `23`; metal avg `0.0008` n `18`; unknown avg `1.0359` n `645`
- 24h: commodity avg `0.1384` n `12`; crypto_alt avg `-1.2648` n `228`; crypto_major avg `-0.5727` n `8`; equity avg `0.2128` n `74`; fx avg `-0.051` n `6`; index avg `0.1287` n `23`; metal avg `-0.1531` n `18`; unknown avg `2.3043` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
