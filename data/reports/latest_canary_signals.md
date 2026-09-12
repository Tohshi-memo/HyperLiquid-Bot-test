# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T06:37:28.745669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.74` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `0.0564` n `233`; crypto_major avg `0.0662` n `8`; equity avg `-0.0106` n `136`; fx avg `0.0012` n `6`; index avg `0.0013` n `26`; metal avg `0.0029` n `20`; unknown avg `-0.0413` n `838`
- 1h: commodity avg `0.0005` n `12`; crypto_alt avg `0.1033` n `233`; crypto_major avg `0.0294` n `8`; equity avg `-0.0416` n `136`; fx avg `-0.0042` n `6`; index avg `0.0081` n `26`; metal avg `0.0045` n `20`; unknown avg `5.3562` n `808`
- 4h: commodity avg `-0.1177` n `12`; crypto_alt avg `0.1251` n `233`; crypto_major avg `-0.0051` n `8`; equity avg `-0.1045` n `136`; fx avg `-0.0042` n `6`; index avg `0.0106` n `26`; metal avg `0.0018` n `20`; unknown avg `2.2454` n `796`
- 24h: commodity avg `-0.4499` n `12`; crypto_alt avg `1.1615` n `233`; crypto_major avg `0.8668` n `8`; equity avg `0.3591` n `136`; fx avg `-0.1444` n `6`; index avg `0.1764` n `26`; metal avg `-0.0389` n `20`; unknown avg `0.6834` n `692`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
