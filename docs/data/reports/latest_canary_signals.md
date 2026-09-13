# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T14:22:30.396551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0755` n `12`; crypto_alt avg `0.1729` n `233`; crypto_major avg `0.2351` n `8`; equity avg `0.0824` n `136`; fx avg `0.0018` n `6`; index avg `0.0072` n `27`; metal avg `0.0136` n `20`; unknown avg `2.2426` n `838`
- 1h: commodity avg `-0.0908` n `12`; crypto_alt avg `0.9468` n `233`; crypto_major avg `0.6975` n `8`; equity avg `0.3557` n `136`; fx avg `0.007` n `6`; index avg `0.0638` n `27`; metal avg `0.0128` n `20`; unknown avg `2.6413` n `836`
- 4h: commodity avg `0.0802` n `12`; crypto_alt avg `0.7874` n `233`; crypto_major avg `0.4079` n `8`; equity avg `0.0744` n `136`; fx avg `0.0079` n `6`; index avg `0.0199` n `27`; metal avg `-0.0044` n `20`; unknown avg `2.2352` n `826`
- 24h: commodity avg `0.2067` n `12`; crypto_alt avg `0.1525` n `233`; crypto_major avg `-1.5413` n `8`; equity avg `-1.6037` n `136`; fx avg `0.0097` n `6`; index avg `-0.2413` n `26`; metal avg `-0.0699` n `20`; unknown avg `2.4974` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
