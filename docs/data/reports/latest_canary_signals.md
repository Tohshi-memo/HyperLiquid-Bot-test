# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T07:52:30.749092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0225` n `13`; crypto_alt avg `0.1154` n `239`; crypto_major avg `0.07` n `8`; equity avg `0.1566` n `157`; fx avg `0.0079` n `6`; index avg `0.0358` n `27`; metal avg `0.0106` n `20`; unknown avg `0.421` n `1264`
- 1h: commodity avg `0.0445` n `13`; crypto_alt avg `0.515` n `239`; crypto_major avg `0.442` n `8`; equity avg `0.2278` n `157`; fx avg `0.0239` n `6`; index avg `0.0203` n `27`; metal avg `-0.0408` n `20`; unknown avg `0.4612` n `1254`
- 4h: commodity avg `0.3471` n `13`; crypto_alt avg `0.0668` n `239`; crypto_major avg `0.12` n `8`; equity avg `-0.3835` n `157`; fx avg `0.04` n `6`; index avg `-0.0352` n `27`; metal avg `-0.2539` n `20`; unknown avg `0.5061` n `1166`
- 24h: commodity avg `-0.52` n `13`; crypto_alt avg `-2.2892` n `238`; crypto_major avg `-1.2565` n `8`; equity avg `-4.1488` n `157`; fx avg `-0.021` n `6`; index avg `-0.3079` n `27`; metal avg `-0.4625` n `20`; unknown avg `8.3838` n `973`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
