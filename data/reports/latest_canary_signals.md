# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T04:25:52.159859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0181` n `12`; crypto_alt avg `0.0308` n `229`; crypto_major avg `0.0888` n `8`; equity avg `0.0186` n `92`; fx avg `-0.0005` n `6`; index avg `0.0061` n `25`; metal avg `0.0058` n `20`; unknown avg `-0.0087` n `765`
- 1h: commodity avg `0.0145` n `12`; crypto_alt avg `0.0271` n `229`; crypto_major avg `0.0316` n `8`; equity avg `-0.0025` n `92`; fx avg `-0.0008` n `6`; index avg `0.0052` n `25`; metal avg `-0.0154` n `20`; unknown avg `0.1225` n `763`
- 4h: commodity avg `-0.0517` n `12`; crypto_alt avg `0.3322` n `229`; crypto_major avg `0.0914` n `8`; equity avg `0.0411` n `92`; fx avg `0.0006` n `6`; index avg `0.0121` n `25`; metal avg `0.0175` n `20`; unknown avg `1.2585` n `763`
- 24h: commodity avg `-0.4022` n `12`; crypto_alt avg `0.4473` n `229`; crypto_major avg `-0.2356` n `8`; equity avg `-0.7866` n `92`; fx avg `-0.1856` n `6`; index avg `0.0042` n `25`; metal avg `-0.0042` n `20`; unknown avg `4.6392` n `730`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
