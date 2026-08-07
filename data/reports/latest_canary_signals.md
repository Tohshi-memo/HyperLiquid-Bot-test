# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T12:26:13.021006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0978` n `12`; crypto_alt avg `-0.0697` n `230`; crypto_major avg `0.1255` n `8`; equity avg `0.0515` n `112`; fx avg `-0.0019` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0849` n `20`; unknown avg `0.0451` n `782`
- 1h: commodity avg `0.1103` n `12`; crypto_alt avg `-0.0909` n `230`; crypto_major avg `0.1957` n `8`; equity avg `-0.002` n `112`; fx avg `0.005` n `6`; index avg `0.0251` n `25`; metal avg `-0.141` n `20`; unknown avg `0.0347` n `782`
- 4h: commodity avg `-0.2238` n `12`; crypto_alt avg `0.1154` n `230`; crypto_major avg `1.0146` n `8`; equity avg `0.2219` n `112`; fx avg `-0.0078` n `6`; index avg `0.0535` n `25`; metal avg `-0.1908` n `20`; unknown avg `0.2169` n `782`
- 24h: commodity avg `0.237` n `12`; crypto_alt avg `0.5314` n `230`; crypto_major avg `0.6854` n `8`; equity avg `2.4334` n `109`; fx avg `-0.0719` n `6`; index avg `0.1564` n `25`; metal avg `0.1858` n `20`; unknown avg `0.4473` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
