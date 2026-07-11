# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T16:30:14.411391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `12`; crypto_alt avg `0.1553` n `230`; crypto_major avg `0.072` n `8`; equity avg `0.0152` n `92`; fx avg `-0.0007` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0252` n `765`
- 1h: commodity avg `-0.0338` n `12`; crypto_alt avg `0.104` n `230`; crypto_major avg `0.0146` n `8`; equity avg `0.0445` n `92`; fx avg `-0.0216` n `6`; index avg `-0.0023` n `25`; metal avg `0.0022` n `20`; unknown avg `-0.0429` n `765`
- 4h: commodity avg `-0.0853` n `12`; crypto_alt avg `0.3065` n `230`; crypto_major avg `0.417` n `8`; equity avg `-0.0652` n `92`; fx avg `-0.0335` n `6`; index avg `0.0142` n `25`; metal avg `-0.0204` n `20`; unknown avg `0.1251` n `765`
- 24h: commodity avg `0.0904` n `12`; crypto_alt avg `0.9935` n `229`; crypto_major avg `0.749` n `8`; equity avg `0.1081` n `92`; fx avg `-0.0498` n `6`; index avg `0.0609` n `25`; metal avg `-0.0104` n `20`; unknown avg `2.2995` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
