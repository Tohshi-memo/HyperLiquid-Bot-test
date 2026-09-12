# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T04:07:28.084224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.91` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.03` n `12`; crypto_alt avg `0.001` n `233`; crypto_major avg `0.0213` n `8`; equity avg `-0.0035` n `136`; fx avg `0.0013` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0072` n `20`; unknown avg `1.8815` n `836`
- 1h: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.0276` n `233`; crypto_major avg `-0.0423` n `8`; equity avg `-0.0498` n `136`; fx avg `0.0046` n `6`; index avg `0.0026` n `26`; metal avg `-0.0169` n `20`; unknown avg `0.5322` n `824`
- 4h: commodity avg `-0.1013` n `12`; crypto_alt avg `0.6267` n `233`; crypto_major avg `0.1416` n `8`; equity avg `-0.0266` n `136`; fx avg `0.0187` n `6`; index avg `0.0063` n `26`; metal avg `-0.0347` n `20`; unknown avg `0.3122` n `814`
- 24h: commodity avg `-0.7223` n `12`; crypto_alt avg `1.1804` n `233`; crypto_major avg `1.2772` n `8`; equity avg `1.1452` n `136`; fx avg `-0.1085` n `6`; index avg `0.3273` n `26`; metal avg `0.2673` n `20`; unknown avg `11.5488` n `690`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
