# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T09:07:28.181189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.66` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `-0.0011` n `233`; crypto_major avg `0.029` n `8`; equity avg `0.0159` n `136`; fx avg `0.0` n `6`; index avg `0.0007` n `26`; metal avg `-0.0029` n `20`; unknown avg `0.1418` n `836`
- 1h: commodity avg `0.0092` n `12`; crypto_alt avg `-0.0824` n `233`; crypto_major avg `0.112` n `8`; equity avg `0.0129` n `136`; fx avg `0.0072` n `6`; index avg `0.0054` n `26`; metal avg `0.0029` n `20`; unknown avg `0.2274` n `830`
- 4h: commodity avg `-0.0372` n `12`; crypto_alt avg `0.6203` n `233`; crypto_major avg `0.474` n `8`; equity avg `-0.0653` n `136`; fx avg `0.0013` n `6`; index avg `0.0118` n `26`; metal avg `0.0081` n `20`; unknown avg `0.2022` n `800`
- 24h: commodity avg `-0.211` n `12`; crypto_alt avg `1.4235` n `233`; crypto_major avg `1.0377` n `8`; equity avg `-0.1024` n `136`; fx avg `-0.0594` n `6`; index avg `0.099` n `26`; metal avg `-0.0526` n `20`; unknown avg `1.0029` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
