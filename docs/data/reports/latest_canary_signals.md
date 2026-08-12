# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T00:06:19.184466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0543` n `12`; crypto_alt avg `0.0118` n `230`; crypto_major avg `-0.0731` n `8`; equity avg `0.0327` n `113`; fx avg `0.0053` n `6`; index avg `-0.0052` n `25`; metal avg `0.0057` n `20`; unknown avg `0.0075` n `786`
- 1h: commodity avg `0.0356` n `12`; crypto_alt avg `0.0259` n `230`; crypto_major avg `0.07` n `8`; equity avg `-0.0442` n `113`; fx avg `0.0054` n `6`; index avg `0.0053` n `25`; metal avg `-0.0071` n `20`; unknown avg `0.0065` n `786`
- 4h: commodity avg `0.0192` n `12`; crypto_alt avg `-0.1054` n `230`; crypto_major avg `0.1006` n `8`; equity avg `0.5594` n `113`; fx avg `0.0005` n `6`; index avg `0.0171` n `25`; metal avg `0.002` n `20`; unknown avg `-0.0039` n `785`
- 24h: commodity avg `0.181` n `12`; crypto_alt avg `-1.1125` n `230`; crypto_major avg `0.8535` n `8`; equity avg `1.6376` n `113`; fx avg `-0.0696` n `6`; index avg `0.1891` n `25`; metal avg `-0.2697` n `20`; unknown avg `-0.0537` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2247`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2174`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2032`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1969`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
