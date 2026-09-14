# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T16:52:33.993986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2212` n `12`; crypto_alt avg `0.4962` n `233`; crypto_major avg `0.416` n `8`; equity avg `0.3535` n `136`; fx avg `-0.0078` n `6`; index avg `0.0699` n `27`; metal avg `0.1047` n `20`; unknown avg `0.8598` n `886`
- 1h: commodity avg `-0.2592` n `12`; crypto_alt avg `0.6098` n `233`; crypto_major avg `0.6132` n `8`; equity avg `0.3699` n `136`; fx avg `-0.0075` n `6`; index avg `0.0947` n `27`; metal avg `0.1793` n `20`; unknown avg `0.9432` n `878`
- 4h: commodity avg `-0.3891` n `12`; crypto_alt avg `0.9819` n `233`; crypto_major avg `1.1226` n `8`; equity avg `1.4807` n `136`; fx avg `-0.0397` n `6`; index avg `0.2029` n `27`; metal avg `0.2715` n `20`; unknown avg `1.2168` n `864`
- 24h: commodity avg `0.1774` n `12`; crypto_alt avg `0.325` n `233`; crypto_major avg `1.9255` n `8`; equity avg `-0.065` n `136`; fx avg `0.0371` n `6`; index avg `-0.1042` n `27`; metal avg `-0.2236` n `20`; unknown avg `1.3018` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
