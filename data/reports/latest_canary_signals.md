# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T18:22:41.161614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.042` n `12`; crypto_alt avg `-0.0026` n `230`; crypto_major avg `0.0578` n `8`; equity avg `-0.0413` n `108`; fx avg `0.0082` n `6`; index avg `-0.0059` n `25`; metal avg `0.0331` n `20`; unknown avg `0.0547` n `782`
- 1h: commodity avg `0.1714` n `12`; crypto_alt avg `0.1659` n `230`; crypto_major avg `0.483` n `8`; equity avg `0.0952` n `108`; fx avg `0.0018` n `6`; index avg `0.0305` n `25`; metal avg `0.158` n `20`; unknown avg `-0.0721` n `782`
- 4h: commodity avg `0.1652` n `12`; crypto_alt avg `0.3315` n `230`; crypto_major avg `0.7767` n `8`; equity avg `-0.3257` n `108`; fx avg `-0.0144` n `6`; index avg `-0.102` n `25`; metal avg `0.1526` n `20`; unknown avg `-0.0758` n `782`
- 24h: commodity avg `0.0474` n `12`; crypto_alt avg `0.6482` n `230`; crypto_major avg `0.9261` n `8`; equity avg `-0.3148` n `108`; fx avg `-0.0096` n `6`; index avg `-0.0646` n `25`; metal avg `0.7936` n `20`; unknown avg `0.7518` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
