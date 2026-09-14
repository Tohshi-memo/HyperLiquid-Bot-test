# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T07:52:30.149348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.037` n `12`; crypto_alt avg `-0.1069` n `233`; crypto_major avg `0.0096` n `8`; equity avg `-0.1003` n `136`; fx avg `-0.0127` n `6`; index avg `-0.0323` n `27`; metal avg `-0.043` n `20`; unknown avg `0.2229` n `894`
- 1h: commodity avg `0.1085` n `12`; crypto_alt avg `-0.2137` n `233`; crypto_major avg `0.087` n `8`; equity avg `-0.3498` n `136`; fx avg `-0.0273` n `6`; index avg `-0.0556` n `27`; metal avg `-0.1233` n `20`; unknown avg `0.2558` n `868`
- 4h: commodity avg `0.039` n `12`; crypto_alt avg `0.0142` n `233`; crypto_major avg `0.4229` n `8`; equity avg `-0.5166` n `136`; fx avg `-0.0154` n `6`; index avg `-0.1002` n `27`; metal avg `-0.1578` n `20`; unknown avg `0.3417` n `832`
- 24h: commodity avg `0.7348` n `12`; crypto_alt avg `-0.3067` n `233`; crypto_major avg `0.7397` n `8`; equity avg `-1.4161` n `136`; fx avg `0.042` n `6`; index avg `-0.3295` n `27`; metal avg `-0.3031` n `20`; unknown avg `0.8639` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
