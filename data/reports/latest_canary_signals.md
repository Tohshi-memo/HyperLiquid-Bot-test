# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T12:22:34.261210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `12`; crypto_alt avg `0.0615` n `230`; crypto_major avg `0.0201` n `8`; equity avg `-0.0454` n `113`; fx avg `-0.0138` n `6`; index avg `-0.0091` n `25`; metal avg `-0.0539` n `20`; unknown avg `-0.0763` n `786`
- 1h: commodity avg `0.1386` n `12`; crypto_alt avg `0.1791` n `230`; crypto_major avg `0.1959` n `8`; equity avg `0.3179` n `113`; fx avg `0.0158` n `6`; index avg `0.029` n `25`; metal avg `-0.0946` n `20`; unknown avg `-0.098` n `786`
- 4h: commodity avg `0.0499` n `12`; crypto_alt avg `0.4153` n `230`; crypto_major avg `0.7094` n `8`; equity avg `0.3516` n `113`; fx avg `-0.004` n `6`; index avg `0.0519` n `25`; metal avg `0.0549` n `20`; unknown avg `-0.1638` n `786`
- 24h: commodity avg `0.2974` n `12`; crypto_alt avg `-0.7746` n `230`; crypto_major avg `0.9147` n `8`; equity avg `2.378` n `113`; fx avg `0.0564` n `6`; index avg `0.1916` n `25`; metal avg `0.1628` n `20`; unknown avg `-0.1182` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.247`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2374`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2103`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
