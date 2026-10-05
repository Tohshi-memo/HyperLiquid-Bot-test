# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T11:37:37.426932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.037` n `13`; crypto_alt avg `0.0569` n `235`; crypto_major avg `0.0803` n `8`; equity avg `0.039` n `144`; fx avg `0.0038` n `6`; index avg `0.0171` n `26`; metal avg `0.0225` n `20`; unknown avg `0.3636` n `1079`
- 1h: commodity avg `-0.123` n `13`; crypto_alt avg `0.2616` n `235`; crypto_major avg `0.1752` n `8`; equity avg `0.1059` n `144`; fx avg `0.0021` n `6`; index avg `0.0644` n `26`; metal avg `0.1192` n `20`; unknown avg `-0.0756` n `1077`
- 4h: commodity avg `0.0605` n `13`; crypto_alt avg `-0.146` n `235`; crypto_major avg `-0.0743` n `8`; equity avg `-0.0806` n `144`; fx avg `0.0556` n `6`; index avg `0.018` n `26`; metal avg `0.1429` n `20`; unknown avg `42.9432` n `997`
- 24h: commodity avg `-0.2057` n `13`; crypto_alt avg `1.1999` n `235`; crypto_major avg `1.0856` n `8`; equity avg `0.1491` n `144`; fx avg `-0.0419` n `6`; index avg `-0.0343` n `26`; metal avg `0.3211` n `20`; unknown avg `0.4533` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2137`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1963`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
