# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T03:07:36.091180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.96` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `0.0199` n `233`; crypto_major avg `0.0826` n `8`; equity avg `-0.0084` n `136`; fx avg `-0.0031` n `6`; index avg `0.0028` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.2021` n `836`
- 1h: commodity avg `0.0165` n `12`; crypto_alt avg `0.0685` n `233`; crypto_major avg `0.0342` n `8`; equity avg `-0.0099` n `136`; fx avg `-0.0007` n `6`; index avg `0.0026` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.0399` n `836`
- 4h: commodity avg `-0.1097` n `12`; crypto_alt avg `1.152` n `233`; crypto_major avg `0.3429` n `8`; equity avg `0.1183` n `136`; fx avg `0.0035` n `6`; index avg `0.0165` n `26`; metal avg `-0.0315` n `20`; unknown avg `-0.1149` n `824`
- 24h: commodity avg `-0.7191` n `12`; crypto_alt avg `1.8789` n `233`; crypto_major avg `1.7152` n `8`; equity avg `1.1691` n `136`; fx avg `-0.1403` n `6`; index avg `0.3432` n `26`; metal avg `0.2858` n `20`; unknown avg `16.2771` n `700`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
