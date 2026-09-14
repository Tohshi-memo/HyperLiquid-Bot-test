# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T12:22:30.362786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0257` n `12`; crypto_alt avg `0.0744` n `233`; crypto_major avg `0.1649` n `8`; equity avg `0.0535` n `136`; fx avg `-0.0166` n `6`; index avg `0.0126` n `27`; metal avg `-0.0174` n `20`; unknown avg `1.4432` n `894`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `0.0982` n `233`; crypto_major avg `0.0916` n `8`; equity avg `-0.2214` n `136`; fx avg `-0.0018` n `6`; index avg `-0.0185` n `27`; metal avg `-0.0157` n `20`; unknown avg `1.0576` n `892`
- 4h: commodity avg `-0.058` n `12`; crypto_alt avg `-0.1804` n `233`; crypto_major avg `0.0927` n `8`; equity avg `-0.3003` n `136`; fx avg `0.0314` n `6`; index avg `-0.0295` n `27`; metal avg `-0.1342` n `20`; unknown avg `4.1684` n `886`
- 24h: commodity avg `0.544` n `12`; crypto_alt avg `0.1222` n `233`; crypto_major avg `1.8203` n `8`; equity avg `-1.0487` n `136`; fx avg `0.0497` n `6`; index avg `-0.2099` n `27`; metal avg `-0.4171` n `20`; unknown avg `0.9154` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
