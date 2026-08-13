# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T07:37:29.918427+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1089` n `12`; crypto_alt avg `0.0478` n `230`; crypto_major avg `-0.0037` n `8`; equity avg `0.1012` n `113`; fx avg `-0.0099` n `6`; index avg `0.0108` n `25`; metal avg `0.0171` n `20`; unknown avg `-0.0097` n `787`
- 1h: commodity avg `-0.1567` n `12`; crypto_alt avg `0.132` n `230`; crypto_major avg `0.1938` n `8`; equity avg `-0.2222` n `113`; fx avg `0.0093` n `6`; index avg `-0.0096` n `25`; metal avg `-0.0359` n `20`; unknown avg `0.0856` n `787`
- 4h: commodity avg `-0.0175` n `12`; crypto_alt avg `0.2669` n `230`; crypto_major avg `0.5077` n `8`; equity avg `-0.4176` n `113`; fx avg `0.0605` n `6`; index avg `-0.0452` n `25`; metal avg `-0.2809` n `20`; unknown avg `0.059` n `754`
- 24h: commodity avg `-0.2484` n `12`; crypto_alt avg `-0.3403` n `230`; crypto_major avg `0.4812` n `8`; equity avg `1.8502` n `113`; fx avg `-0.0087` n `6`; index avg `0.2453` n `25`; metal avg `-0.4228` n `20`; unknown avg `0.0652` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2467`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1967`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1935`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
