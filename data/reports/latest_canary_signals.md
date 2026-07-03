# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T15:52:28.479473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `-0.1334` n `229`; crypto_major avg `-0.1571` n `8`; equity avg `-0.0349` n `88`; fx avg `0.0004` n `6`; index avg `-0.0213` n `25`; metal avg `-0.046` n `20`; unknown avg `0.7116` n `765`
- 1h: commodity avg `0.0127` n `12`; crypto_alt avg `0.0271` n `229`; crypto_major avg `-0.0834` n `8`; equity avg `-0.0014` n `88`; fx avg `-0.0017` n `6`; index avg `-0.0211` n `25`; metal avg `-0.0709` n `20`; unknown avg `0.8301` n `765`
- 4h: commodity avg `0.0848` n `12`; crypto_alt avg `0.2863` n `229`; crypto_major avg `0.1125` n `8`; equity avg `-0.175` n `88`; fx avg `-0.0252` n `6`; index avg `-0.0257` n `25`; metal avg `-0.1333` n `20`; unknown avg `1.8573` n `765`
- 24h: commodity avg `0.4309` n `12`; crypto_alt avg `2.5265` n `229`; crypto_major avg `2.0426` n `8`; equity avg `1.0904` n `88`; fx avg `-0.0533` n `6`; index avg `0.379` n `25`; metal avg `0.4717` n `20`; unknown avg `8.0864` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
