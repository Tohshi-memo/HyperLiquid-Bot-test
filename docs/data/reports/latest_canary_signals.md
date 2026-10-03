# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T08:22:30.245043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.09` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0017` n `13`; crypto_alt avg `0.0366` n `235`; crypto_major avg `-0.0652` n `8`; equity avg `-0.0084` n `143`; fx avg `0.0022` n `6`; index avg `-0.0018` n `26`; metal avg `0.0024` n `20`; unknown avg `0.0234` n `984`
- 1h: commodity avg `0.004` n `13`; crypto_alt avg `-0.1926` n `235`; crypto_major avg `-0.0505` n `8`; equity avg `-0.0089` n `143`; fx avg `0.0039` n `6`; index avg `-0.0056` n `26`; metal avg `0.0042` n `20`; unknown avg `0.0559` n `966`
- 4h: commodity avg `-0.0154` n `13`; crypto_alt avg `-0.3529` n `235`; crypto_major avg `-0.0441` n `8`; equity avg `0.0172` n `143`; fx avg `-0.0045` n `6`; index avg `-0.0128` n `26`; metal avg `0.0144` n `20`; unknown avg `0.1006` n `944`
- 24h: commodity avg `0.5671` n `13`; crypto_alt avg `-2.5944` n `235`; crypto_major avg `-2.6193` n `8`; equity avg `-0.0324` n `142`; fx avg `0.0169` n `6`; index avg `0.1266` n `26`; metal avg `-0.3564` n `20`; unknown avg `-0.4539` n `872`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
