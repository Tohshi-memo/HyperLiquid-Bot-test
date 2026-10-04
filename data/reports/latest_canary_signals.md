# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T02:37:30.396143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `13`; crypto_alt avg `0.1583` n `235`; crypto_major avg `0.0124` n `8`; equity avg `0.0028` n `143`; fx avg `0.0019` n `6`; index avg `-0.0012` n `26`; metal avg `0.0044` n `20`; unknown avg `0.4158` n `1079`
- 1h: commodity avg `0.0061` n `13`; crypto_alt avg `0.1248` n `235`; crypto_major avg `0.0717` n `8`; equity avg `0.0099` n `143`; fx avg `0.0038` n `6`; index avg `0.0017` n `26`; metal avg `0.007` n `20`; unknown avg `0.6803` n `1077`
- 4h: commodity avg `-0.0008` n `13`; crypto_alt avg `0.0202` n `235`; crypto_major avg `-0.0389` n `8`; equity avg `-0.0107` n `143`; fx avg `-0.0126` n `6`; index avg `-0.0126` n `26`; metal avg `0.0075` n `20`; unknown avg `-0.0996` n `1071`
- 24h: commodity avg `0.1627` n `13`; crypto_alt avg `1.3752` n `235`; crypto_major avg `0.5121` n `8`; equity avg `0.1156` n `143`; fx avg `-0.0259` n `6`; index avg `0.0018` n `26`; metal avg `-0.0071` n `20`; unknown avg `-0.003` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2015`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
