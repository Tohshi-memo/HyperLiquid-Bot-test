# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T07:07:29.182903+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.65` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `0.0531` n `233`; crypto_major avg `0.034` n `8`; equity avg `-0.0152` n `136`; fx avg `-0.0063` n `6`; index avg `0.0009` n `26`; metal avg `0.0035` n `20`; unknown avg `0.1833` n `836`
- 1h: commodity avg `-0.0385` n `12`; crypto_alt avg `0.3656` n `233`; crypto_major avg `0.1749` n `8`; equity avg `-0.034` n `136`; fx avg `0.0043` n `6`; index avg `0.0012` n `26`; metal avg `0.014` n `20`; unknown avg `-0.1841` n `834`
- 4h: commodity avg `-0.1078` n `12`; crypto_alt avg `0.2297` n `233`; crypto_major avg `0.0013` n `8`; equity avg `-0.1293` n `136`; fx avg `-0.0023` n `6`; index avg `0.0085` n `26`; metal avg `0.0066` n `20`; unknown avg `1.8883` n `796`
- 24h: commodity avg `-0.4011` n `12`; crypto_alt avg `1.0546` n `233`; crypto_major avg `0.7112` n `8`; equity avg `0.1269` n `136`; fx avg `-0.1252` n `6`; index avg `0.1476` n `26`; metal avg `-0.0551` n `20`; unknown avg `0.7867` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
