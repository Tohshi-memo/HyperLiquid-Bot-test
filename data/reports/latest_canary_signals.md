# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T16:07:32.138457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0284` n `13`; crypto_alt avg `0.4212` n `235`; crypto_major avg `0.4071` n `8`; equity avg `0.0685` n `150`; fx avg `-0.0048` n `6`; index avg `0.0065` n `26`; metal avg `0.0024` n `20`; unknown avg `0.0829` n `1110`
- 1h: commodity avg `0.0205` n `13`; crypto_alt avg `1.0644` n `235`; crypto_major avg `1.0647` n `8`; equity avg `0.1611` n `150`; fx avg `-0.0085` n `6`; index avg `0.0181` n `26`; metal avg `0.0143` n `20`; unknown avg `2.0203` n `1110`
- 4h: commodity avg `-0.0458` n `13`; crypto_alt avg `1.9491` n `235`; crypto_major avg `1.2359` n `8`; equity avg `0.177` n `150`; fx avg `-0.0262` n `6`; index avg `0.0166` n `26`; metal avg `0.0172` n `20`; unknown avg `2.7155` n `1037`
- 24h: commodity avg `0.2448` n `13`; crypto_alt avg `2.2408` n `235`; crypto_major avg `0.9057` n `8`; equity avg `0.2231` n `150`; fx avg `0.0095` n `6`; index avg `0.0072` n `26`; metal avg `0.0328` n `20`; unknown avg `1.2347` n `925`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
