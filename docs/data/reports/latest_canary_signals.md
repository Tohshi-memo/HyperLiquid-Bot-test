# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T19:22:30.976403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `13`; crypto_alt avg `-0.1117` n `237`; crypto_major avg `-0.0262` n `8`; equity avg `-0.0367` n `152`; fx avg `-0.0039` n `6`; index avg `-0.0049` n `26`; metal avg `-0.0039` n `20`; unknown avg `0.9156` n `1231`
- 1h: commodity avg `-0.0835` n `13`; crypto_alt avg `0.3182` n `237`; crypto_major avg `0.4116` n `8`; equity avg `0.2431` n `152`; fx avg `-0.0134` n `6`; index avg `0.0385` n `26`; metal avg `0.0175` n `20`; unknown avg `6.2752` n `1231`
- 4h: commodity avg `0.0217` n `13`; crypto_alt avg `1.2681` n `237`; crypto_major avg `1.5066` n `8`; equity avg `0.3777` n `152`; fx avg `-0.027` n `6`; index avg `0.0477` n `26`; metal avg `0.0359` n `20`; unknown avg `2.1575` n `1200`
- 24h: commodity avg `0.1501` n `13`; crypto_alt avg `-2.6297` n `237`; crypto_major avg `-1.5451` n `8`; equity avg `-0.368` n `152`; fx avg `-0.0481` n `6`; index avg `-0.0363` n `26`; metal avg `-0.1786` n `20`; unknown avg `101.7497` n `1046`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1822`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
