# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T08:22:29.434515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.0112` n `230`; crypto_major avg `-0.0392` n `8`; equity avg `0.0266` n `112`; fx avg `-0.0044` n `6`; index avg `-0.0131` n `25`; metal avg `0.0117` n `20`; unknown avg `0.0219` n `784`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `0.0217` n `230`; crypto_major avg `-0.0592` n `8`; equity avg `0.0463` n `112`; fx avg `-0.0007` n `6`; index avg `-0.0003` n `25`; metal avg `0.0157` n `20`; unknown avg `0.1574` n `784`
- 4h: commodity avg `0.0167` n `12`; crypto_alt avg `0.1456` n `230`; crypto_major avg `0.0487` n `8`; equity avg `-0.0542` n `112`; fx avg `-0.0025` n `6`; index avg `-0.0331` n `25`; metal avg `-0.0079` n `20`; unknown avg `0.0306` n `751`
- 24h: commodity avg `-0.188` n `12`; crypto_alt avg `-0.0395` n `230`; crypto_major avg `0.5487` n `8`; equity avg `0.7937` n `112`; fx avg `-0.0443` n `6`; index avg `0.0509` n `25`; metal avg `-0.052` n `20`; unknown avg `0.0721` n `750`

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
