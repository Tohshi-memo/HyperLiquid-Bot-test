# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T06:52:28.736349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.7` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `0.0112` n `233`; crypto_major avg `0.0202` n `8`; equity avg `-0.009` n `136`; fx avg `0.0081` n `6`; index avg `0.0005` n `26`; metal avg `-0.0005` n `20`; unknown avg `-0.3227` n `838`
- 1h: commodity avg `-0.0256` n `12`; crypto_alt avg `0.2203` n `233`; crypto_major avg `0.0536` n `8`; equity avg `-0.0342` n `136`; fx avg `0.0047` n `6`; index avg `0.0017` n `26`; metal avg `0.0093` n `20`; unknown avg `1.9158` n `808`
- 4h: commodity avg `-0.0956` n `12`; crypto_alt avg `0.1942` n `233`; crypto_major avg `0.0498` n `8`; equity avg `-0.1225` n `136`; fx avg `0.0008` n `6`; index avg `0.0104` n `26`; metal avg `0.0021` n `20`; unknown avg `2.1047` n `796`
- 24h: commodity avg `-0.4633` n `12`; crypto_alt avg `1.157` n `233`; crypto_major avg `0.7651` n `8`; equity avg `0.2374` n `136`; fx avg `-0.1474` n `6`; index avg `0.1622` n `26`; metal avg `-0.0566` n `20`; unknown avg `0.6375` n `692`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
