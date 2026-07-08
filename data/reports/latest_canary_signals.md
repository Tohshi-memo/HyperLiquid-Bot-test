# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T23:52:25.084290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `0.0653` n `229`; crypto_major avg `0.1581` n `8`; equity avg `0.1272` n `91`; fx avg `-0.0174` n `6`; index avg `-0.0325` n `25`; metal avg `-0.0086` n `20`; unknown avg `0.1179` n `764`
- 1h: commodity avg `-0.0417` n `12`; crypto_alt avg `0.0076` n `229`; crypto_major avg `0.1646` n `8`; equity avg `0.1401` n `91`; fx avg `-0.0168` n `6`; index avg `-0.0223` n `25`; metal avg `-0.0426` n `20`; unknown avg `0.1105` n `764`
- 4h: commodity avg `0.0574` n `12`; crypto_alt avg `0.2322` n `229`; crypto_major avg `0.2972` n `8`; equity avg `0.4329` n `91`; fx avg `-0.0104` n `6`; index avg `-0.0032` n `25`; metal avg `-0.0484` n `20`; unknown avg `-0.1045` n `764`
- 24h: commodity avg `0.3267` n `12`; crypto_alt avg `-1.3535` n `229`; crypto_major avg `-1.9577` n `8`; equity avg `2.0037` n `91`; fx avg `-0.087` n `6`; index avg `0.0573` n `25`; metal avg `-0.6827` n `20`; unknown avg `-0.0703` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
