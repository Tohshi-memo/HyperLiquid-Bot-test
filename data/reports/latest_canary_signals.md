# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T12:22:29.443128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.56` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0007` n `13`; crypto_alt avg `0.229` n `239`; crypto_major avg `0.0096` n `8`; equity avg `0.0365` n `168`; fx avg `0.001` n `6`; index avg `0.0039` n `27`; metal avg `0.0052` n `20`; unknown avg `3.1852` n `1267`
- 1h: commodity avg `0.0052` n `13`; crypto_alt avg `0.2369` n `239`; crypto_major avg `0.3079` n `8`; equity avg `0.0596` n `168`; fx avg `0.0026` n `6`; index avg `0.0046` n `27`; metal avg `0.0063` n `20`; unknown avg `11.0898` n `1255`
- 4h: commodity avg `-0.0291` n `13`; crypto_alt avg `-0.1757` n `239`; crypto_major avg `-0.3264` n `8`; equity avg `-0.0717` n `168`; fx avg `0.0063` n `6`; index avg `-0.0137` n `27`; metal avg `0.0311` n `20`; unknown avg `347.1554` n `1227`
- 24h: commodity avg `-0.4762` n `13`; crypto_alt avg `-3.294` n `239`; crypto_major avg `-3.0695` n `8`; equity avg `0.0514` n `168`; fx avg `-0.1017` n `6`; index avg `0.0293` n `27`; metal avg `-0.1031` n `20`; unknown avg `190.8886` n `1087`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
