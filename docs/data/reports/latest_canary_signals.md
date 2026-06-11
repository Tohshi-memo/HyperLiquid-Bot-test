# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T09:52:29.565685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1296` n `12`; crypto_alt avg `0.0532` n `228`; crypto_major avg `0.0826` n `8`; equity avg `0.0969` n `74`; fx avg `-0.0004` n `6`; index avg `0.0311` n `23`; metal avg `0.1277` n `18`; unknown avg `-0.1525` n `556`
- 1h: commodity avg `0.055` n `12`; crypto_alt avg `0.0217` n `228`; crypto_major avg `-0.0093` n `8`; equity avg `-0.0598` n `74`; fx avg `0.0006` n `6`; index avg `0.0146` n `23`; metal avg `-0.1726` n `18`; unknown avg `4.6497` n `556`
- 4h: commodity avg `-0.5712` n `12`; crypto_alt avg `0.4985` n `228`; crypto_major avg `0.5841` n `8`; equity avg `0.8451` n `74`; fx avg `-0.0249` n `6`; index avg `0.3927` n `23`; metal avg `-0.1935` n `18`; unknown avg `4.8735` n `530`
- 24h: commodity avg `0.3097` n `12`; crypto_alt avg `1.8297` n `228`; crypto_major avg `1.8031` n `8`; equity avg `1.0195` n `74`; fx avg `-0.0055` n `6`; index avg `0.1597` n `23`; metal avg `-0.3054` n `18`; unknown avg `8.5256` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
