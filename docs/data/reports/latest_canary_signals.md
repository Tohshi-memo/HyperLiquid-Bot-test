# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T02:22:31.724942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.09` n `12`; crypto_alt avg `-0.3213` n `228`; crypto_major avg `-0.3881` n `8`; equity avg `-0.4821` n `74`; fx avg `-0.0081` n `6`; index avg `-0.1289` n `23`; metal avg `-0.2186` n `18`; unknown avg `-0.1995` n `550`
- 1h: commodity avg `-0.0396` n `12`; crypto_alt avg `-0.0166` n `228`; crypto_major avg `-0.0746` n `8`; equity avg `-0.7306` n `74`; fx avg `0.0162` n `6`; index avg `-0.2075` n `23`; metal avg `-0.2625` n `18`; unknown avg `-0.156` n `550`
- 4h: commodity avg `-0.1346` n `12`; crypto_alt avg `2.4395` n `228`; crypto_major avg `1.6757` n `8`; equity avg `0.6266` n `74`; fx avg `0.1819` n `6`; index avg `0.4123` n `23`; metal avg `1.212` n `18`; unknown avg `0.4655` n `550`
- 24h: commodity avg `1.5337` n `12`; crypto_alt avg `-0.598` n `228`; crypto_major avg `-0.6691` n `8`; equity avg `-1.5282` n `74`; fx avg `0.0961` n `6`; index avg `-1.2722` n `23`; metal avg `-0.7778` n `18`; unknown avg `-0.0211` n `537`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2135`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1893`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
