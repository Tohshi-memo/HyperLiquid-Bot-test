# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T05:22:29.462713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0205` n `13`; crypto_alt avg `0.1187` n `238`; crypto_major avg `0.0968` n `8`; equity avg `0.1875` n `154`; fx avg `-0.0095` n `6`; index avg `0.0314` n `27`; metal avg `0.0187` n `20`; unknown avg `0.2493` n `1236`
- 1h: commodity avg `0.0084` n `13`; crypto_alt avg `0.1948` n `238`; crypto_major avg `0.0864` n `8`; equity avg `0.1172` n `154`; fx avg `-0.0131` n `6`; index avg `0.0058` n `27`; metal avg `-0.0236` n `20`; unknown avg `72.2965` n `1234`
- 4h: commodity avg `0.0221` n `13`; crypto_alt avg `0.1074` n `238`; crypto_major avg `0.1767` n `8`; equity avg `0.6232` n `154`; fx avg `0.0544` n `6`; index avg `0.0182` n `27`; metal avg `-0.1821` n `20`; unknown avg `31.7423` n `1214`
- 24h: commodity avg `0.0459` n `13`; crypto_alt avg `2.2007` n `237`; crypto_major avg `2.0947` n `8`; equity avg `3.5551` n `154`; fx avg `0.1024` n `6`; index avg `0.4536` n `27`; metal avg `0.2306` n `20`; unknown avg `16.1457` n `1016`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
