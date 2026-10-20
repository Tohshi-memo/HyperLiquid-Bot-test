# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T12:22:29.108588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0593` n `13`; crypto_alt avg `0.1806` n `237`; crypto_major avg `0.0876` n `8`; equity avg `-0.0044` n `151`; fx avg `0.0119` n `6`; index avg `-0.0172` n `26`; metal avg `-0.0357` n `20`; unknown avg `0.0874` n `1198`
- 1h: commodity avg `-0.0956` n `13`; crypto_alt avg `0.2364` n `237`; crypto_major avg `0.1336` n `8`; equity avg `-0.1499` n `151`; fx avg `0.0142` n `6`; index avg `-0.0473` n `26`; metal avg `-0.0903` n `20`; unknown avg `-0.4868` n `1188`
- 4h: commodity avg `0.0943` n `13`; crypto_alt avg `-0.0338` n `237`; crypto_major avg `0.023` n `8`; equity avg `-0.7017` n `151`; fx avg `0.0029` n `6`; index avg `-0.1269` n `26`; metal avg `-0.1382` n `20`; unknown avg `0.973` n `1188`
- 24h: commodity avg `0.2508` n `13`; crypto_alt avg `0.0501` n `237`; crypto_major avg `-0.8259` n `8`; equity avg `-2.6587` n `151`; fx avg `-0.0098` n `6`; index avg `-0.3631` n `26`; metal avg `-0.3556` n `20`; unknown avg `0.5389` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
