# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T14:07:32.264559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1671` n `12`; crypto_alt avg `-0.2795` n `229`; crypto_major avg `-0.1931` n `8`; equity avg `-0.4539` n `91`; fx avg `-0.0038` n `6`; index avg `-0.0545` n `25`; metal avg `-0.1493` n `20`; unknown avg `-0.0023` n `763`
- 1h: commodity avg `0.4607` n `12`; crypto_alt avg `-0.4392` n `229`; crypto_major avg `-0.2798` n `8`; equity avg `-1.1296` n `91`; fx avg `-0.0011` n `6`; index avg `-0.1234` n `25`; metal avg `-0.0866` n `20`; unknown avg `0.0708` n `763`
- 4h: commodity avg `0.2767` n `12`; crypto_alt avg `-0.4654` n `229`; crypto_major avg `-0.4377` n `8`; equity avg `-1.3217` n `91`; fx avg `-0.0454` n `6`; index avg `-0.136` n `25`; metal avg `0.1021` n `20`; unknown avg `-0.09` n `763`
- 24h: commodity avg `0.5265` n `12`; crypto_alt avg `0.6351` n `229`; crypto_major avg `0.9042` n `8`; equity avg `-3.0098` n `90`; fx avg `-0.1796` n `6`; index avg `-0.5449` n `25`; metal avg `0.0785` n `20`; unknown avg `0.1726` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
