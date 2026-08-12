# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T18:07:32.189837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `-0.0265` n `230`; crypto_major avg `-0.0873` n `8`; equity avg `-0.08` n `113`; fx avg `0.0001` n `6`; index avg `-0.0098` n `25`; metal avg `-0.027` n `20`; unknown avg `0.0355` n `786`
- 1h: commodity avg `0.0462` n `12`; crypto_alt avg `-0.0075` n `230`; crypto_major avg `0.0254` n `8`; equity avg `0.2379` n `113`; fx avg `0.0028` n `6`; index avg `-0.003` n `25`; metal avg `-0.0245` n `20`; unknown avg `0.1943` n `786`
- 4h: commodity avg `0.0384` n `12`; crypto_alt avg `-0.152` n `230`; crypto_major avg `0.1861` n `8`; equity avg `0.6801` n `113`; fx avg `-0.0151` n `6`; index avg `0.0072` n `25`; metal avg `-0.2432` n `20`; unknown avg `0.2241` n `786`
- 24h: commodity avg `0.0435` n `12`; crypto_alt avg `-0.0957` n `230`; crypto_major avg `0.7779` n `8`; equity avg `3.8752` n `113`; fx avg `0.0345` n `6`; index avg `0.4203` n `25`; metal avg `0.2313` n `20`; unknown avg `0.2453` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.227`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
