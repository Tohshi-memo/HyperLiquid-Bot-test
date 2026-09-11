# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T17:22:27.635175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.32` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0726` n `12`; crypto_alt avg `-0.3819` n `233`; crypto_major avg `-0.2128` n `8`; equity avg `0.0521` n `136`; fx avg `-0.008` n `6`; index avg `0.0086` n `26`; metal avg `0.0301` n `20`; unknown avg `0.2073` n `782`
- 1h: commodity avg `-0.0741` n `12`; crypto_alt avg `0.1171` n `233`; crypto_major avg `0.2748` n `8`; equity avg `0.1888` n `136`; fx avg `-0.0043` n `6`; index avg `0.0285` n `26`; metal avg `0.0855` n `20`; unknown avg `0.3082` n `774`
- 4h: commodity avg `0.0249` n `12`; crypto_alt avg `0.6357` n `233`; crypto_major avg `0.6114` n `8`; equity avg `-0.0576` n `136`; fx avg `0.0244` n `6`; index avg `0.0121` n `26`; metal avg `-0.1169` n `20`; unknown avg `0.9246` n `758`
- 24h: commodity avg `-0.4326` n `12`; crypto_alt avg `1.1483` n `233`; crypto_major avg `1.8837` n `8`; equity avg `0.4989` n `136`; fx avg `-0.1514` n `6`; index avg `0.3062` n `26`; metal avg `0.1229` n `20`; unknown avg `1.9896` n `686`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
