# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T11:07:34.475279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0416` n `12`; crypto_alt avg `-0.1862` n `228`; crypto_major avg `-0.1781` n `8`; equity avg `-0.0202` n `74`; fx avg `-0.0191` n `6`; index avg `-0.0073` n `23`; metal avg `-0.0478` n `18`; unknown avg `-0.1545` n `645`
- 1h: commodity avg `0.1242` n `12`; crypto_alt avg `-0.2228` n `228`; crypto_major avg `-0.095` n `8`; equity avg `0.0529` n `74`; fx avg `-0.0098` n `6`; index avg `0.0415` n `23`; metal avg `-0.0731` n `18`; unknown avg `0.1878` n `645`
- 4h: commodity avg `0.0012` n `12`; crypto_alt avg `0.0942` n `228`; crypto_major avg `0.164` n `8`; equity avg `0.3402` n `74`; fx avg `-0.0217` n `6`; index avg `0.0709` n `23`; metal avg `-0.0497` n `18`; unknown avg `0.4143` n `629`
- 24h: commodity avg `-0.5528` n `12`; crypto_alt avg `0.1061` n `228`; crypto_major avg `0.8865` n `8`; equity avg `0.9726` n `74`; fx avg `-0.0392` n `6`; index avg `0.2368` n `23`; metal avg `0.1158` n `18`; unknown avg `-0.7793` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
