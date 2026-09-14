# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T07:37:26.018769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0359` n `12`; crypto_alt avg `-0.0825` n `233`; crypto_major avg `0.0118` n `8`; equity avg `-0.0362` n `136`; fx avg `-0.0085` n `6`; index avg `-0.0042` n `27`; metal avg `-0.0595` n `20`; unknown avg `0.2434` n `894`
- 1h: commodity avg `0.1602` n `12`; crypto_alt avg `0.0006` n `233`; crypto_major avg `0.2791` n `8`; equity avg `-0.2481` n `136`; fx avg `-0.0105` n `6`; index avg `-0.0261` n `27`; metal avg `-0.1184` n `20`; unknown avg `0.6104` n `868`
- 4h: commodity avg `0.0325` n `12`; crypto_alt avg `0.053` n `233`; crypto_major avg `0.2923` n `8`; equity avg `-0.4412` n `136`; fx avg `-0.0054` n `6`; index avg `-0.0784` n `27`; metal avg `-0.1214` n `20`; unknown avg `0.2388` n `828`
- 24h: commodity avg `0.6801` n `12`; crypto_alt avg `-0.2194` n `233`; crypto_major avg `0.7597` n `8`; equity avg `-1.3575` n `136`; fx avg `0.0567` n `6`; index avg `-0.3039` n `27`; metal avg `-0.262` n `20`; unknown avg `0.8041` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
