# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T01:07:37.764603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0325` n `12`; crypto_alt avg `0.1473` n `232`; crypto_major avg `0.1775` n `8`; equity avg `0.0911` n `133`; fx avg `0.0059` n `6`; index avg `0.0279` n `26`; metal avg `0.0127` n `20`; unknown avg `1.2972` n `790`
- 1h: commodity avg `0.004` n `12`; crypto_alt avg `0.0055` n `232`; crypto_major avg `-0.086` n `8`; equity avg `0.0071` n `133`; fx avg `-0.0706` n `6`; index avg `0.0127` n `26`; metal avg `0.0533` n `20`; unknown avg `0.925` n `790`
- 4h: commodity avg `0.0418` n `12`; crypto_alt avg `0.3385` n `232`; crypto_major avg `0.0631` n `8`; equity avg `0.325` n `133`; fx avg `0.0054` n `6`; index avg `0.0176` n `26`; metal avg `0.0218` n `20`; unknown avg `0.4335` n `786`
- 24h: commodity avg `-0.0336` n `12`; crypto_alt avg `0.4554` n `232`; crypto_major avg `0.0296` n `8`; equity avg `1.1429` n `133`; fx avg `-0.348` n `6`; index avg `0.0916` n `26`; metal avg `0.6085` n `20`; unknown avg `-0.0805` n `751`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0491`, n `668`, weak_sample_signal
