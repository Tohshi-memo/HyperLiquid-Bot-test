# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T07:02:48.329663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0497` n `12`; crypto_alt avg `-0.0264` n `230`; crypto_major avg `-0.0148` n `8`; equity avg `-0.149` n `121`; fx avg `0.0083` n `6`; index avg `-0.0289` n `25`; metal avg `-0.0263` n `20`; unknown avg `-0.0131` n `792`
- 1h: commodity avg `0.0822` n `12`; crypto_alt avg `0.5231` n `230`; crypto_major avg `0.7126` n `8`; equity avg `0.0943` n `121`; fx avg `-0.0213` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0505` n `20`; unknown avg `0.3258` n `792`
- 4h: commodity avg `0.1086` n `12`; crypto_alt avg `0.7166` n `230`; crypto_major avg `1.2168` n `8`; equity avg `0.1451` n `121`; fx avg `-0.0081` n `6`; index avg `0.0083` n `25`; metal avg `-0.0798` n `20`; unknown avg `0.2422` n `776`
- 24h: commodity avg `-0.0158` n `12`; crypto_alt avg `5.8011` n `230`; crypto_major avg `10.5525` n `8`; equity avg `1.088` n `120`; fx avg `0.0655` n `6`; index avg `0.2236` n `25`; metal avg `1.015` n `20`; unknown avg `1.9349` n `773`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1983`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
