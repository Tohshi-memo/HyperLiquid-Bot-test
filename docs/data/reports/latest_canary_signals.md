# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T10:07:29.059987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.0383` n `228`; crypto_major avg `-0.0147` n `8`; equity avg `-0.0357` n `86`; fx avg `-0.0025` n `6`; index avg `-0.0085` n `23`; metal avg `-0.007` n `20`; unknown avg `-0.0441` n `765`
- 1h: commodity avg `-0.0632` n `12`; crypto_alt avg `-0.5312` n `228`; crypto_major avg `-0.519` n `8`; equity avg `-0.0226` n `86`; fx avg `-0.0017` n `6`; index avg `-0.0126` n `23`; metal avg `0.1328` n `20`; unknown avg `-0.1129` n `765`
- 4h: commodity avg `-0.3518` n `12`; crypto_alt avg `0.5306` n `228`; crypto_major avg `0.3858` n `8`; equity avg `0.2698` n `86`; fx avg `-0.031` n `6`; index avg `0.0756` n `23`; metal avg `0.7149` n `20`; unknown avg `0.0392` n `749`
- 24h: commodity avg `-0.0579` n `12`; crypto_alt avg `-2.1666` n `228`; crypto_major avg `-2.3627` n `8`; equity avg `-4.1612` n `86`; fx avg `0.0255` n `6`; index avg `-0.599` n `23`; metal avg `0.6044` n `20`; unknown avg `0.7169` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2704`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2082`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
