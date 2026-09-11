# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T17:07:32.960620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.2` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.0094` n `233`; crypto_major avg `-0.0158` n `8`; equity avg `0.109` n `136`; fx avg `0.0003` n `6`; index avg `0.0169` n `26`; metal avg `0.0113` n `20`; unknown avg `-0.006` n `794`
- 1h: commodity avg `-0.0603` n `12`; crypto_alt avg `0.0108` n `233`; crypto_major avg `-0.1019` n `8`; equity avg `-0.1106` n `136`; fx avg `-0.0022` n `6`; index avg `-0.015` n `26`; metal avg `-0.0177` n `20`; unknown avg `0.1274` n `788`
- 4h: commodity avg `0.184` n `12`; crypto_alt avg `1.1266` n `233`; crypto_major avg `0.9056` n `8`; equity avg `-0.2887` n `136`; fx avg `0.0585` n `6`; index avg `-0.0183` n `26`; metal avg `-0.1282` n `20`; unknown avg `0.7857` n `772`
- 24h: commodity avg `-0.3381` n `12`; crypto_alt avg `1.6557` n `233`; crypto_major avg `2.3044` n `8`; equity avg `0.3923` n `136`; fx avg `-0.1506` n `6`; index avg `0.2859` n `26`; metal avg `0.0887` n `20`; unknown avg `2.8389` n `697`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
