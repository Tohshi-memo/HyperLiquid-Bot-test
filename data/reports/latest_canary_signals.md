# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T09:07:26.561206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0843` n `13`; crypto_alt avg `0.0519` n `239`; crypto_major avg `0.0658` n `8`; equity avg `0.1444` n `168`; fx avg `0.0027` n `6`; index avg `0.0065` n `27`; metal avg `-0.0241` n `20`; unknown avg `162.3463` n `1239`
- 1h: commodity avg `-0.1099` n `13`; crypto_alt avg `0.0728` n `239`; crypto_major avg `-0.0662` n `8`; equity avg `0.5842` n `168`; fx avg `-0.0148` n `6`; index avg `0.07` n `27`; metal avg `0.1317` n `20`; unknown avg `176.9097` n `1133`
- 4h: commodity avg `-0.2112` n `13`; crypto_alt avg `0.1083` n `239`; crypto_major avg `0.173` n `8`; equity avg `0.7001` n `168`; fx avg `-0.064` n `6`; index avg `0.0185` n `27`; metal avg `0.4182` n `20`; unknown avg `181.2945` n `1105`
- 24h: commodity avg `0.375` n `13`; crypto_alt avg `2.0154` n `239`; crypto_major avg `2.5344` n `8`; equity avg `4.1066` n `168`; fx avg `-0.0728` n `6`; index avg `0.3363` n `27`; metal avg `1.2491` n `20`; unknown avg `48.3647` n `1029`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
