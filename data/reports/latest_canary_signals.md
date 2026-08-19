# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T05:18:57.129571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `0.039` n `230`; crypto_major avg `-0.0237` n `8`; equity avg `-0.232` n `120`; fx avg `-0.025` n `6`; index avg `-0.0423` n `25`; metal avg `-0.0587` n `20`; unknown avg `0.1739` n `789`
- 1h: commodity avg `-0.004` n `12`; crypto_alt avg `0.0134` n `230`; crypto_major avg `-0.0592` n `8`; equity avg `-0.3513` n `120`; fx avg `-0.0371` n `6`; index avg `-0.0508` n `25`; metal avg `-0.1389` n `20`; unknown avg `0.0645` n `789`
- 4h: commodity avg `-0.04` n `12`; crypto_alt avg `-0.0585` n `230`; crypto_major avg `-0.1473` n `8`; equity avg `-0.8328` n `120`; fx avg `-0.122` n `6`; index avg `-0.1789` n `25`; metal avg `-0.0315` n `20`; unknown avg `-0.1693` n `789`
- 24h: commodity avg `0.2437` n `12`; crypto_alt avg `0.5048` n `230`; crypto_major avg `0.1768` n `8`; equity avg `-3.4237` n `120`; fx avg `-0.1712` n `6`; index avg `-0.5435` n `25`; metal avg `-0.693` n `20`; unknown avg `-0.2451` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
