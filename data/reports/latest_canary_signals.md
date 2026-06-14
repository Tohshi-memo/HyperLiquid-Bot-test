# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T13:22:32.872274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0392` n `12`; crypto_alt avg `-0.0792` n `228`; crypto_major avg `-0.0264` n `8`; equity avg `0.009` n `74`; fx avg `-0.0061` n `6`; index avg `-0.0048` n `23`; metal avg `-0.0013` n `18`; unknown avg `0.0301` n `645`
- 1h: commodity avg `0.209` n `12`; crypto_alt avg `-0.6276` n `228`; crypto_major avg `-0.3986` n `8`; equity avg `-0.0881` n `74`; fx avg `-0.0148` n `6`; index avg `0.035` n `23`; metal avg `-0.0717` n `18`; unknown avg `0.1405` n `645`
- 4h: commodity avg `0.2944` n `12`; crypto_alt avg `-0.3699` n `228`; crypto_major avg `-0.0313` n `8`; equity avg `0.1105` n `74`; fx avg `0.0201` n `6`; index avg `0.1551` n `23`; metal avg `-0.1036` n `18`; unknown avg `0.3296` n `629`
- 24h: commodity avg `-0.1609` n `12`; crypto_alt avg `-0.9386` n `228`; crypto_major avg `-0.2462` n `8`; equity avg `0.6717` n `74`; fx avg `-0.0098` n `6`; index avg `0.1783` n `23`; metal avg `-0.0776` n `18`; unknown avg `-1.1343` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
