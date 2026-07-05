# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T09:07:26.850480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `12`; crypto_alt avg `0.0582` n `229`; crypto_major avg `-0.0411` n `8`; equity avg `-0.0118` n `88`; fx avg `0.0` n `6`; index avg `-0.0062` n `25`; metal avg `0.0033` n `20`; unknown avg `0.0308` n `765`
- 1h: commodity avg `0.0394` n `12`; crypto_alt avg `-0.0512` n `229`; crypto_major avg `0.019` n `8`; equity avg `0.0348` n `88`; fx avg `0.0015` n `6`; index avg `-0.0027` n `25`; metal avg `0.0238` n `20`; unknown avg `-0.0301` n `765`
- 4h: commodity avg `0.0443` n `12`; crypto_alt avg `0.1147` n `229`; crypto_major avg `0.2538` n `8`; equity avg `0.0616` n `88`; fx avg `0.0129` n `6`; index avg `-0.0185` n `25`; metal avg `0.0196` n `20`; unknown avg `-0.0198` n `731`
- 24h: commodity avg `0.1162` n `12`; crypto_alt avg `-0.3605` n `229`; crypto_major avg `-0.5585` n `8`; equity avg `0.2462` n `88`; fx avg `0.0178` n `6`; index avg `0.0487` n `25`; metal avg `0.0781` n `20`; unknown avg `-1.3252` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
