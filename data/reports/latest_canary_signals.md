# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T11:52:28.494084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0436` n `12`; crypto_alt avg `0.1068` n `230`; crypto_major avg `0.0658` n `8`; equity avg `0.175` n `113`; fx avg `0.0123` n `6`; index avg `0.0141` n `25`; metal avg `0.0257` n `20`; unknown avg `-0.0107` n `786`
- 1h: commodity avg `0.0119` n `12`; crypto_alt avg `0.0418` n `230`; crypto_major avg `0.0974` n `8`; equity avg `0.1955` n `113`; fx avg `0.0161` n `6`; index avg `0.0324` n `25`; metal avg `0.1434` n `20`; unknown avg `-0.0238` n `786`
- 4h: commodity avg `-0.0363` n `12`; crypto_alt avg `0.2096` n `230`; crypto_major avg `0.6541` n `8`; equity avg `0.571` n `113`; fx avg `-0.0089` n `6`; index avg `0.1028` n `25`; metal avg `0.2147` n `20`; unknown avg `-0.0132` n `786`
- 24h: commodity avg `0.3464` n `12`; crypto_alt avg `-1.0117` n `230`; crypto_major avg `0.8334` n `8`; equity avg `2.3498` n `113`; fx avg `0.0849` n `6`; index avg `0.2089` n `25`; metal avg `0.2742` n `20`; unknown avg `-0.1042` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2454`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2346`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1864`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
