# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T08:19:22.905268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `0.0052` n `230`; crypto_major avg `-0.0223` n `8`; equity avg `0.0333` n `112`; fx avg `-0.0012` n `6`; index avg `-0.0127` n `25`; metal avg `0.0112` n `20`; unknown avg `0.0115` n `784`
- 1h: commodity avg `0.0113` n `12`; crypto_alt avg `0.0384` n `230`; crypto_major avg `-0.0423` n `8`; equity avg `0.0531` n `112`; fx avg `0.0025` n `6`; index avg `0.0002` n `25`; metal avg `0.0152` n `20`; unknown avg `0.1485` n `784`
- 4h: commodity avg `0.0184` n `12`; crypto_alt avg `0.1627` n `230`; crypto_major avg `0.0655` n `8`; equity avg `-0.0474` n `112`; fx avg `0.0007` n `6`; index avg `-0.0327` n `25`; metal avg `-0.0084` n `20`; unknown avg `0.0218` n `751`
- 24h: commodity avg `-0.1864` n `12`; crypto_alt avg `-0.0234` n `230`; crypto_major avg `0.5659` n `8`; equity avg `0.8008` n `112`; fx avg `-0.0411` n `6`; index avg `0.0514` n `25`; metal avg `-0.0525` n `20`; unknown avg `0.0613` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
