# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T15:37:30.728168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0537` n `12`; crypto_alt avg `0.0612` n `229`; crypto_major avg `-0.0206` n `8`; equity avg `-0.0137` n `88`; fx avg `-0.0104` n `6`; index avg `-0.019` n `25`; metal avg `-0.0399` n `20`; unknown avg `0.0863` n `765`
- 1h: commodity avg `-0.0554` n `12`; crypto_alt avg `0.3083` n `229`; crypto_major avg `0.3539` n `8`; equity avg `0.0733` n `88`; fx avg `-0.0083` n `6`; index avg `0.0057` n `25`; metal avg `0.0149` n `20`; unknown avg `0.0738` n `765`
- 4h: commodity avg `0.0431` n `12`; crypto_alt avg `0.567` n `229`; crypto_major avg `0.4792` n `8`; equity avg `-0.1582` n `88`; fx avg `-0.0279` n `6`; index avg `-0.0059` n `25`; metal avg `-0.1012` n `20`; unknown avg `1.2371` n `765`
- 24h: commodity avg `0.44` n `12`; crypto_alt avg `2.549` n `229`; crypto_major avg `2.0768` n `8`; equity avg `0.648` n `88`; fx avg `-0.0491` n `6`; index avg `0.2921` n `25`; metal avg `0.3868` n `20`; unknown avg `7.95` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
