# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T02:07:29.095040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0443` n `12`; crypto_alt avg `-0.509` n `230`; crypto_major avg `-0.433` n `8`; equity avg `-0.2744` n `92`; fx avg `0.0054` n `6`; index avg `-0.0428` n `25`; metal avg `-0.1079` n `20`; unknown avg `0.2257` n `766`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.9488` n `230`; crypto_major avg `-0.9812` n `8`; equity avg `-0.8245` n `92`; fx avg `0.0192` n `6`; index avg `-0.1977` n `25`; metal avg `-0.0543` n `20`; unknown avg `0.8759` n `766`
- 4h: commodity avg `-0.0384` n `12`; crypto_alt avg `-0.5949` n `230`; crypto_major avg `-0.4963` n `8`; equity avg `-1.7206` n `92`; fx avg `0.1018` n `6`; index avg `-0.3919` n `25`; metal avg `-0.1132` n `20`; unknown avg `-0.0158` n `765`
- 24h: commodity avg `0.0068` n `12`; crypto_alt avg `-1.4879` n `230`; crypto_major avg `-0.6957` n `8`; equity avg `-1.9156` n `92`; fx avg `0.0159` n `6`; index avg `-0.4388` n `25`; metal avg `-0.3271` n `20`; unknown avg `0.0071` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
