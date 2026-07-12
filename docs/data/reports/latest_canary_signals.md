# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T07:37:32.874135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0292` n `12`; crypto_alt avg `-0.1075` n `230`; crypto_major avg `-0.0943` n `8`; equity avg `0.0045` n `92`; fx avg `0.0` n `6`; index avg `0.023` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.0234` n `765`
- 1h: commodity avg `0.0621` n `12`; crypto_alt avg `0.068` n `230`; crypto_major avg `0.135` n `8`; equity avg `0.0196` n `92`; fx avg `0.0039` n `6`; index avg `0.0117` n `25`; metal avg `0.0002` n `20`; unknown avg `2.5768` n `763`
- 4h: commodity avg `0.115` n `12`; crypto_alt avg `-0.5965` n `230`; crypto_major avg `-0.4669` n `8`; equity avg `-0.1577` n `92`; fx avg `-0.0024` n `6`; index avg `0.0103` n `25`; metal avg `-0.0197` n `20`; unknown avg `-0.3115` n `747`
- 24h: commodity avg `0.4897` n `12`; crypto_alt avg `-0.7073` n `230`; crypto_major avg `-0.7211` n `8`; equity avg `-0.17` n `92`; fx avg `0.0018` n `6`; index avg `-0.1236` n `25`; metal avg `-0.0909` n `20`; unknown avg `-0.0387` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
