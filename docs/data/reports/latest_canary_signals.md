# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T14:22:30.902900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0832` n `13`; crypto_alt avg `0.1006` n `235`; crypto_major avg `0.0546` n `8`; equity avg `0.0155` n `143`; fx avg `-0.0076` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.0333` n `982`
- 1h: commodity avg `0.1435` n `13`; crypto_alt avg `0.3636` n `235`; crypto_major avg `0.1466` n `8`; equity avg `0.014` n `143`; fx avg `-0.0082` n `6`; index avg `0.0072` n `26`; metal avg `-0.0024` n `20`; unknown avg `0.0896` n `964`
- 4h: commodity avg `0.1347` n `13`; crypto_alt avg `0.2675` n `235`; crypto_major avg `0.2282` n `8`; equity avg `0.0013` n `143`; fx avg `-0.0199` n `6`; index avg `0.0039` n `26`; metal avg `0.0007` n `20`; unknown avg `0.164` n `954`
- 24h: commodity avg `0.9715` n `13`; crypto_alt avg `-2.3235` n `235`; crypto_major avg `-2.1662` n `8`; equity avg `-0.7226` n `143`; fx avg `-0.0322` n `6`; index avg `-0.1093` n `26`; metal avg `-0.311` n `20`; unknown avg `0.8011` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.197`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1865`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
