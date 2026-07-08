# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T21:35:23.102855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0369` n `12`; crypto_alt avg `0.1688` n `229`; crypto_major avg `0.0554` n `8`; equity avg `0.1034` n `91`; fx avg `0.0137` n `6`; index avg `0.0034` n `25`; metal avg `-0.0256` n `20`; unknown avg `0.0378` n `764`
- 1h: commodity avg `0.0284` n `12`; crypto_alt avg `-0.1444` n `229`; crypto_major avg `-0.187` n `8`; equity avg `0.2312` n `91`; fx avg `0.0281` n `6`; index avg `0.0195` n `25`; metal avg `0.0307` n `20`; unknown avg `-0.1259` n `764`
- 4h: commodity avg `0.2613` n `12`; crypto_alt avg `-0.6116` n `229`; crypto_major avg `-0.6745` n `8`; equity avg `0.4458` n `91`; fx avg `-0.01` n `6`; index avg `-0.0234` n `25`; metal avg `-0.0266` n `20`; unknown avg `0.9618` n `764`
- 24h: commodity avg `0.4708` n `12`; crypto_alt avg `-2.0427` n `229`; crypto_major avg `-2.4622` n `8`; equity avg `1.2802` n `91`; fx avg `0.0242` n `6`; index avg `-0.032` n `25`; metal avg `-0.8621` n `20`; unknown avg `0.1052` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
