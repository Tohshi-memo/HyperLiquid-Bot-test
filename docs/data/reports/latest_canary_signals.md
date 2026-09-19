# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T16:47:26.604070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.0475` n `234`; crypto_major avg `-0.0116` n `8`; equity avg `-0.0002` n `140`; fx avg `0.0006` n `6`; index avg `0.002` n `26`; metal avg `0.0003` n `20`; unknown avg `-0.1022` n `935`
- 1h: commodity avg `-0.0136` n `12`; crypto_alt avg `0.3742` n `234`; crypto_major avg `0.038` n `8`; equity avg `0.0101` n `140`; fx avg `-0.0021` n `6`; index avg `0.0069` n `26`; metal avg `-0.0161` n `20`; unknown avg `4.0823` n `917`
- 4h: commodity avg `-0.164` n `12`; crypto_alt avg `0.1595` n `234`; crypto_major avg `0.1916` n `8`; equity avg `0.0343` n `140`; fx avg `-0.0094` n `6`; index avg `0.014` n `26`; metal avg `-0.0054` n `20`; unknown avg `4.8744` n `914`
- 24h: commodity avg `-0.1081` n `12`; crypto_alt avg `3.0232` n `234`; crypto_major avg `1.6147` n `8`; equity avg `0.6602` n `140`; fx avg `0.0204` n `6`; index avg `0.1606` n `26`; metal avg `-0.0643` n `20`; unknown avg `1.6687` n `798`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1762`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
