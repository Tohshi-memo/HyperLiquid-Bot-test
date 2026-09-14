# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T11:22:28.543849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0648` n `12`; crypto_alt avg `0.1827` n `233`; crypto_major avg `0.2359` n `8`; equity avg `-0.0755` n `136`; fx avg `0.0067` n `6`; index avg `-0.0022` n `27`; metal avg `0.0545` n `20`; unknown avg `0.0297` n `894`
- 1h: commodity avg `0.0415` n `12`; crypto_alt avg `-0.077` n `233`; crypto_major avg `-0.0463` n `8`; equity avg `-0.0553` n `136`; fx avg `0.0289` n `6`; index avg `0.0327` n `27`; metal avg `0.0781` n `20`; unknown avg `0.3326` n `892`
- 4h: commodity avg `0.0393` n `12`; crypto_alt avg `-0.4283` n `233`; crypto_major avg `0.0999` n `8`; equity avg `-0.4383` n `136`; fx avg `-0.0024` n `6`; index avg `-0.048` n `27`; metal avg `-0.267` n `20`; unknown avg `7.1168` n `886`
- 24h: commodity avg `0.5391` n `12`; crypto_alt avg `0.2506` n `233`; crypto_major avg `1.8715` n `8`; equity avg `-0.9136` n `136`; fx avg `0.0449` n `6`; index avg `-0.2127` n `27`; metal avg `-0.4082` n `20`; unknown avg `1.1807` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
