# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T16:22:29.104664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0256` n `12`; crypto_alt avg `0.2513` n `228`; crypto_major avg `0.099` n `8`; equity avg `-0.0077` n `74`; fx avg `-0.0244` n `6`; index avg `-0.0126` n `23`; metal avg `0.007` n `18`; unknown avg `0.0604` n `645`
- 1h: commodity avg `-0.0742` n `12`; crypto_alt avg `0.3555` n `228`; crypto_major avg `0.1719` n `8`; equity avg `0.0013` n `74`; fx avg `-0.0165` n `6`; index avg `0.0388` n `23`; metal avg `-0.0444` n `18`; unknown avg `-0.0407` n `645`
- 4h: commodity avg `0.2961` n `12`; crypto_alt avg `-0.672` n `228`; crypto_major avg `-0.594` n `8`; equity avg `-0.1837` n `74`; fx avg `-0.0575` n `6`; index avg `0.0879` n `23`; metal avg `-0.1541` n `18`; unknown avg `-0.0085` n `645`
- 24h: commodity avg `-0.067` n `12`; crypto_alt avg `-0.9676` n `228`; crypto_major avg `-0.3594` n `8`; equity avg `0.4029` n `74`; fx avg `-0.0335` n `6`; index avg `0.1678` n `23`; metal avg `-0.0658` n `18`; unknown avg `1.562` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
