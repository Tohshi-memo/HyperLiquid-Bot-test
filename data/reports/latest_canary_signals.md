# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T00:37:33.266470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `0.0653` n `233`; crypto_major avg `-0.0141` n `8`; equity avg `-0.0063` n `136`; fx avg `0.0017` n `6`; index avg `0.0022` n `26`; metal avg `-0.0004` n `20`; unknown avg `39.1682` n `832`
- 1h: commodity avg `0.0357` n `12`; crypto_alt avg `0.3134` n `233`; crypto_major avg `-0.0392` n `8`; equity avg `-0.0159` n `130`; fx avg `0.0053` n `6`; index avg `-0.0055` n `26`; metal avg `0.001` n `20`; unknown avg `49.8145` n `827`
- 4h: commodity avg `0.0039` n `12`; crypto_alt avg `0.1965` n `233`; crypto_major avg `-0.033` n `8`; equity avg `-0.0187` n `136`; fx avg `0.0004` n `6`; index avg `-0.0053` n `26`; metal avg `-0.0143` n `20`; unknown avg `2.5821` n `796`
- 24h: commodity avg `-0.0288` n `12`; crypto_alt avg `1.1868` n `233`; crypto_major avg `0.2052` n `8`; equity avg `-0.3932` n `136`; fx avg `-0.0004` n `6`; index avg `-0.04` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.6787` n `724`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0428`, n `668`, weak_sample_signal
