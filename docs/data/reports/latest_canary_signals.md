# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T21:37:26.262201+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `13`; crypto_alt avg `0.0673` n `237`; crypto_major avg `0.0492` n `8`; equity avg `0.0382` n `152`; fx avg `-0.0002` n `6`; index avg `0.0097` n `26`; metal avg `0.0033` n `20`; unknown avg `-0.0058` n `1209`
- 1h: commodity avg `0.0079` n `13`; crypto_alt avg `-0.2037` n `237`; crypto_major avg `-0.0633` n `8`; equity avg `-0.0824` n `152`; fx avg `0.0051` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0244` n `20`; unknown avg `0.3704` n `1201`
- 4h: commodity avg `-0.0252` n `13`; crypto_alt avg `1.0777` n `237`; crypto_major avg `0.9211` n `8`; equity avg `0.3105` n `152`; fx avg `0.0055` n `6`; index avg `0.0451` n `26`; metal avg `0.019` n `20`; unknown avg `1.072` n `1159`
- 24h: commodity avg `0.0703` n `13`; crypto_alt avg `-2.3278` n `237`; crypto_major avg `-1.6054` n `8`; equity avg `-0.3049` n `152`; fx avg `-0.0335` n `6`; index avg `-0.0559` n `26`; metal avg `-0.1649` n `20`; unknown avg `0.4336` n `1076`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1911`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
