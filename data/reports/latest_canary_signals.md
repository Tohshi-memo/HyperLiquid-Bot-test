# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T11:37:25.885621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0748` n `12`; crypto_alt avg `0.0452` n `228`; crypto_major avg `0.0688` n `8`; equity avg `-0.0367` n `78`; fx avg `0.0` n `6`; index avg `0.0002` n `23`; metal avg `-0.0013` n `18`; unknown avg `0.182` n `687`
- 1h: commodity avg `-0.1346` n `12`; crypto_alt avg `0.0029` n `228`; crypto_major avg `0.0592` n `8`; equity avg `-0.0538` n `78`; fx avg `0.009` n `6`; index avg `0.0121` n `23`; metal avg `0.0014` n `18`; unknown avg `-0.0913` n `687`
- 4h: commodity avg `-0.1673` n `12`; crypto_alt avg `0.0258` n `228`; crypto_major avg `-0.0414` n `8`; equity avg `-0.1682` n `78`; fx avg `0.3242` n `6`; index avg `0.0046` n `23`; metal avg `-0.0199` n `18`; unknown avg `-0.37` n `687`
- 24h: commodity avg `0.3704` n `12`; crypto_alt avg `-3.0697` n `228`; crypto_major avg `-3.345` n `8`; equity avg `1.1053` n `78`; fx avg `-0.0719` n `6`; index avg `0.2935` n `23`; metal avg `-4.1022` n `18`; unknown avg `-0.1507` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
