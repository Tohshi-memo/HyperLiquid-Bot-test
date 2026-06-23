# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T18:37:33.249291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0376` n `12`; crypto_alt avg `0.0209` n `228`; crypto_major avg `-0.1373` n `8`; equity avg `-0.1685` n `86`; fx avg `-0.0011` n `6`; index avg `-0.0042` n `23`; metal avg `-0.0365` n `20`; unknown avg `-0.1845` n `764`
- 1h: commodity avg `0.0259` n `12`; crypto_alt avg `0.037` n `228`; crypto_major avg `-0.219` n `8`; equity avg `-0.5521` n `86`; fx avg `-0.0047` n `6`; index avg `-0.0793` n `23`; metal avg `-0.1173` n `20`; unknown avg `-0.2822` n `764`
- 4h: commodity avg `-0.008` n `12`; crypto_alt avg `-0.8461` n `228`; crypto_major avg `-0.8645` n `8`; equity avg `-1.1365` n `86`; fx avg `-0.0403` n `6`; index avg `-0.1564` n `23`; metal avg `-0.0389` n `20`; unknown avg `-0.8592` n `764`
- 24h: commodity avg `-0.3411` n `12`; crypto_alt avg `-3.8304` n `228`; crypto_major avg `-4.6881` n `8`; equity avg `-3.738` n `86`; fx avg `-0.1778` n `6`; index avg `-0.9397` n `23`; metal avg `-1.1436` n `20`; unknown avg `-0.4537` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
