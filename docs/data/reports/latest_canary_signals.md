# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T15:31:12.697712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `12`; crypto_alt avg `0.103` n `230`; crypto_major avg `0.1531` n `8`; equity avg `-0.0085` n `92`; fx avg `-0.0029` n `6`; index avg `0.0036` n `25`; metal avg `-0.0044` n `20`; unknown avg `-0.0261` n `765`
- 1h: commodity avg `-0.0175` n `12`; crypto_alt avg `0.4072` n `230`; crypto_major avg `0.4719` n `8`; equity avg `0.0247` n `92`; fx avg `-0.0042` n `6`; index avg `0.0168` n `25`; metal avg `0.0094` n `20`; unknown avg `0.0352` n `765`
- 4h: commodity avg `-0.0836` n `12`; crypto_alt avg `0.373` n `230`; crypto_major avg `0.6597` n `8`; equity avg `0.0288` n `92`; fx avg `0.0067` n `6`; index avg `0.0377` n `25`; metal avg `-0.0085` n `20`; unknown avg `-0.0721` n `765`
- 24h: commodity avg `0.4393` n `12`; crypto_alt avg `-0.7561` n `230`; crypto_major avg `-0.2421` n `8`; equity avg `0.0147` n `92`; fx avg `0.0222` n `6`; index avg `-0.1025` n `25`; metal avg `-0.0842` n `20`; unknown avg `0.1405` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
