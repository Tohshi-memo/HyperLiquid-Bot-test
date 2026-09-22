# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T05:07:34.019085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `0.0029` n `234`; crypto_major avg `-0.1208` n `8`; equity avg `0.0282` n `140`; fx avg `-0.0293` n `6`; index avg `-0.0014` n `26`; metal avg `0.0322` n `20`; unknown avg `23.1219` n `942`
- 1h: commodity avg `0.0541` n `12`; crypto_alt avg `-0.4927` n `234`; crypto_major avg `-0.8084` n `8`; equity avg `-0.3752` n `140`; fx avg `-0.0528` n `6`; index avg `-0.0426` n `26`; metal avg `0.0569` n `20`; unknown avg `21.9823` n `942`
- 4h: commodity avg `0.1109` n `12`; crypto_alt avg `-0.1369` n `234`; crypto_major avg `-0.3662` n `8`; equity avg `-0.6597` n `140`; fx avg `-0.0543` n `6`; index avg `-0.1005` n `26`; metal avg `-0.1607` n `20`; unknown avg `22.261` n `936`
- 24h: commodity avg `-0.1631` n `12`; crypto_alt avg `2.9557` n `234`; crypto_major avg `4.271` n `8`; equity avg `1.9065` n `140`; fx avg `-0.2869` n `6`; index avg `0.4103` n `26`; metal avg `-0.002` n `20`; unknown avg `15.5936` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
