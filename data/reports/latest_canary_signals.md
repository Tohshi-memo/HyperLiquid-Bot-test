# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T10:52:26.468138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0447` n `12`; crypto_alt avg `-0.0092` n `228`; crypto_major avg `-0.0788` n `8`; equity avg `-0.0682` n `86`; fx avg `0.0016` n `6`; index avg `0.0146` n `23`; metal avg `-0.0395` n `20`; unknown avg `-0.001` n `764`
- 1h: commodity avg `-0.0316` n `12`; crypto_alt avg `-0.3528` n `228`; crypto_major avg `-0.38` n `8`; equity avg `-0.0092` n `86`; fx avg `-0.0371` n `6`; index avg `0.0314` n `23`; metal avg `-0.235` n `20`; unknown avg `-0.0471` n `764`
- 4h: commodity avg `-0.1209` n `12`; crypto_alt avg `-0.6148` n `228`; crypto_major avg `-0.6373` n `8`; equity avg `-0.1684` n `86`; fx avg `-0.0654` n `6`; index avg `0.0322` n `23`; metal avg `-0.5077` n `20`; unknown avg `-0.3729` n `756`
- 24h: commodity avg `-0.5594` n `12`; crypto_alt avg `0.0654` n `228`; crypto_major avg `-0.0175` n `8`; equity avg `4.9498` n `86`; fx avg `-0.0356` n `6`; index avg `0.1823` n `23`; metal avg `-0.7574` n `20`; unknown avg `-0.1111` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
