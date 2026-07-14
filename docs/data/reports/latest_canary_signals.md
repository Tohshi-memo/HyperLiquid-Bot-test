# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T17:22:29.061376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.1698` n `230`; crypto_major avg `-0.1788` n `8`; equity avg `-0.0605` n `92`; fx avg `-0.0195` n `6`; index avg `0.0093` n `25`; metal avg `0.0127` n `20`; unknown avg `0.2574` n `766`
- 1h: commodity avg `-0.0786` n `12`; crypto_alt avg `-0.2868` n `230`; crypto_major avg `-0.4379` n `8`; equity avg `-0.0207` n `92`; fx avg `-0.0147` n `6`; index avg `0.0684` n `25`; metal avg `0.0031` n `20`; unknown avg `0.2268` n `766`
- 4h: commodity avg `-0.1916` n `12`; crypto_alt avg `-0.2258` n `230`; crypto_major avg `-0.1787` n `8`; equity avg `-0.3528` n `92`; fx avg `-0.0246` n `6`; index avg `0.0891` n `25`; metal avg `-0.0443` n `20`; unknown avg `-0.2249` n `758`
- 24h: commodity avg `0.514` n `12`; crypto_alt avg `1.352` n `230`; crypto_major avg `2.6323` n `8`; equity avg `0.8299` n `92`; fx avg `-0.0366` n `6`; index avg `0.3076` n `25`; metal avg `0.5756` n `20`; unknown avg `-0.1215` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1864`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
