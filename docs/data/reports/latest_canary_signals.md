# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T00:52:25.861753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0836` n `12`; crypto_alt avg `0.1244` n `230`; crypto_major avg `0.066` n `8`; equity avg `0.0116` n `112`; fx avg `-0.0089` n `6`; index avg `0.0104` n `25`; metal avg `-0.0535` n `20`; unknown avg `0.0173` n `782`
- 1h: commodity avg `-0.0247` n `12`; crypto_alt avg `0.3931` n `230`; crypto_major avg `0.1042` n `8`; equity avg `-0.2617` n `112`; fx avg `-0.0189` n `6`; index avg `-0.0374` n `25`; metal avg `-0.152` n `20`; unknown avg `0.0134` n `782`
- 4h: commodity avg `0.0613` n `12`; crypto_alt avg `0.3816` n `230`; crypto_major avg `-0.0299` n `8`; equity avg `0.2847` n `112`; fx avg `-0.0195` n `6`; index avg `-0.0149` n `25`; metal avg `-0.1221` n `20`; unknown avg `0.0138` n `782`
- 24h: commodity avg `0.6596` n `12`; crypto_alt avg `0.2688` n `230`; crypto_major avg `-1.0885` n `8`; equity avg `0.78` n `109`; fx avg `0.07` n `6`; index avg `-0.0598` n `25`; metal avg `-0.3941` n `20`; unknown avg `113.0738` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
