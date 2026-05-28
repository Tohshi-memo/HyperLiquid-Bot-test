# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T13:52:22.333171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1333` n `12`; crypto_alt avg `0.2805` n `228`; crypto_major avg `0.3067` n `8`; equity avg `0.1143` n `67`; fx avg `-0.0177` n `6`; index avg `-0.0311` n `23`; metal avg `0.1833` n `18`; unknown avg `-0.0483` n `419`
- 1h: commodity avg `0.4407` n `12`; crypto_alt avg `-0.1277` n `228`; crypto_major avg `-0.1824` n `8`; equity avg `-0.212` n `67`; fx avg `0.0016` n `6`; index avg `-0.1276` n `23`; metal avg `-0.1727` n `18`; unknown avg `-0.0015` n `419`
- 4h: commodity avg `0.6477` n `12`; crypto_alt avg `-0.6087` n `228`; crypto_major avg `-0.3381` n `8`; equity avg `0.1205` n `67`; fx avg `0.0739` n `6`; index avg `0.0433` n `23`; metal avg `-0.0313` n `18`; unknown avg `-0.2906` n `419`
- 24h: commodity avg `0.7804` n `12`; crypto_alt avg `-4.8482` n `228`; crypto_major avg `-3.0011` n `8`; equity avg `-0.5911` n `67`; fx avg `0.0019` n `6`; index avg `-0.3888` n `23`; metal avg `-1.0012` n `18`; unknown avg `-1.6058` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1788`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
