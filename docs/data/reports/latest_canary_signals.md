# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T01:25:29.592257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.062` n `12`; crypto_alt avg `0.3951` n `232`; crypto_major avg `0.2665` n `8`; equity avg `-0.0389` n `133`; fx avg `-0.0326` n `6`; index avg `-0.0004` n `26`; metal avg `0.004` n `20`; unknown avg `15.5895` n `792`
- 1h: commodity avg `0.0476` n `12`; crypto_alt avg `0.5397` n `232`; crypto_major avg `0.3926` n `8`; equity avg `0.155` n `133`; fx avg `-0.0642` n `6`; index avg `0.0525` n `26`; metal avg `0.0492` n `20`; unknown avg `15.5984` n `790`
- 4h: commodity avg `0.1192` n `12`; crypto_alt avg `0.6764` n `232`; crypto_major avg `0.3301` n `8`; equity avg `0.1013` n `133`; fx avg `-0.0215` n `6`; index avg `-0.0031` n `26`; metal avg `0.0186` n `20`; unknown avg `15.2126` n `790`
- 24h: commodity avg `0.0401` n `12`; crypto_alt avg `0.7116` n `232`; crypto_major avg `0.2107` n `8`; equity avg `1.081` n `133`; fx avg `-0.3775` n `6`; index avg `0.0953` n `26`; metal avg `0.5955` n `20`; unknown avg `-0.3511` n `751`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
