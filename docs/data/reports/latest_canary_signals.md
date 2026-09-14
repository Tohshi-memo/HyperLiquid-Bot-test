# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T11:37:34.332196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0251` n `12`; crypto_alt avg `-0.0178` n `233`; crypto_major avg `0.0012` n `8`; equity avg `0.0366` n `136`; fx avg `0.0087` n `6`; index avg `-0.002` n `27`; metal avg `-0.0417` n `20`; unknown avg `0.4778` n `894`
- 1h: commodity avg `0.0916` n `12`; crypto_alt avg `-0.1825` n `233`; crypto_major avg `-0.0427` n `8`; equity avg `-0.1453` n `136`; fx avg `0.0232` n `6`; index avg `0.0003` n `27`; metal avg `0.0042` n `20`; unknown avg `0.8018` n `892`
- 4h: commodity avg `0.0285` n `12`; crypto_alt avg `-0.3646` n `233`; crypto_major avg `0.0892` n `8`; equity avg `-0.3672` n `136`; fx avg `0.0148` n `6`; index avg `-0.0458` n `27`; metal avg `-0.2493` n `20`; unknown avg `6.7537` n `886`
- 24h: commodity avg `0.5616` n `12`; crypto_alt avg `0.1691` n `233`; crypto_major avg `1.7897` n `8`; equity avg `-0.8631` n `136`; fx avg `0.0591` n `6`; index avg `-0.2215` n `27`; metal avg `-0.4473` n `20`; unknown avg `1.1339` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
