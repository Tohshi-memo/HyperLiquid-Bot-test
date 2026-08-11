# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T09:11:10.522487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0329` n `12`; crypto_alt avg `-0.0102` n `230`; crypto_major avg `0.0412` n `8`; equity avg `-0.1518` n `113`; fx avg `-0.004` n `6`; index avg `-0.0211` n `25`; metal avg `-0.0431` n `20`; unknown avg `-0.0238` n `785`
- 1h: commodity avg `0.0777` n `12`; crypto_alt avg `0.0624` n `230`; crypto_major avg `0.1327` n `8`; equity avg `-0.3827` n `113`; fx avg `0.0045` n `6`; index avg `-0.0341` n `25`; metal avg `0.0535` n `20`; unknown avg `0.006` n `785`
- 4h: commodity avg `0.3933` n `12`; crypto_alt avg `-0.4014` n `230`; crypto_major avg `-0.0022` n `8`; equity avg `-0.6807` n `113`; fx avg `0.0288` n `6`; index avg `-0.1005` n `25`; metal avg `-0.1296` n `20`; unknown avg `-0.0164` n `753`
- 24h: commodity avg `1.1189` n `12`; crypto_alt avg `-1.2695` n `230`; crypto_major avg `-0.8663` n `8`; equity avg `-1.7374` n `113`; fx avg `0.0062` n `6`; index avg `-0.0837` n `25`; metal avg `0.2371` n `20`; unknown avg `0.1282` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
