# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T08:22:29.739912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.036` n `12`; crypto_alt avg `0.1423` n `233`; crypto_major avg `0.1218` n `8`; equity avg `0.0461` n `136`; fx avg `-0.0122` n `6`; index avg `0.0333` n `27`; metal avg `0.0746` n `20`; unknown avg `18.3224` n `908`
- 1h: commodity avg `0.0542` n `12`; crypto_alt avg `-0.5338` n `233`; crypto_major avg `-0.4037` n `8`; equity avg `-0.2765` n `136`; fx avg `0.0177` n `6`; index avg `-0.0411` n `27`; metal avg `-0.1191` n `20`; unknown avg `4.2248` n `906`
- 4h: commodity avg `0.1043` n `12`; crypto_alt avg `-0.9324` n `233`; crypto_major avg `-0.9593` n `8`; equity avg `-0.5368` n `136`; fx avg `0.1038` n `6`; index avg `-0.0995` n `27`; metal avg `-0.2579` n `20`; unknown avg `19.6383` n `876`
- 24h: commodity avg `-0.036` n `12`; crypto_alt avg `-1.7584` n `233`; crypto_major avg `-1.1809` n `8`; equity avg `-0.1824` n `136`; fx avg `0.2397` n `6`; index avg `-0.0782` n `27`; metal avg `-0.3064` n `20`; unknown avg `3.9659` n `820`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
