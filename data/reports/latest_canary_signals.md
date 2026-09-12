# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T06:07:23.706020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.78` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.0903` n `233`; crypto_major avg `-0.0871` n `8`; equity avg `-0.0154` n `136`; fx avg `-0.0058` n `6`; index avg `0.0014` n `26`; metal avg `-0.0012` n `20`; unknown avg `2.0683` n `808`
- 1h: commodity avg `-0.0163` n `12`; crypto_alt avg `-0.0155` n `233`; crypto_major avg `0.0047` n `8`; equity avg `-0.0685` n `136`; fx avg `-0.0079` n `6`; index avg `0.0085` n `26`; metal avg `-0.0051` n `20`; unknown avg `1.9312` n `808`
- 4h: commodity avg `-0.0529` n `12`; crypto_alt avg `-0.0686` n `233`; crypto_major avg `-0.1389` n `8`; equity avg `-0.1053` n `136`; fx avg `-0.0073` n `6`; index avg `0.0099` n `26`; metal avg `-0.0082` n `20`; unknown avg `2.3229` n `796`
- 24h: commodity avg `-0.3819` n `12`; crypto_alt avg `0.6466` n `233`; crypto_major avg `0.6243` n `8`; equity avg `0.3371` n `136`; fx avg `-0.146` n `6`; index avg `0.1859` n `26`; metal avg `-0.0668` n `20`; unknown avg `1.1636` n `692`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
