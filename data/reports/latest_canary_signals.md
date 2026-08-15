# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T16:52:28.050777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `0.0159` n `230`; crypto_major avg `0.0787` n `8`; equity avg `-0.0041` n `114`; fx avg `0.0018` n `6`; index avg `-0.0001` n `25`; metal avg `-0.003` n `20`; unknown avg `7.3546` n `791`
- 1h: commodity avg `0.0078` n `12`; crypto_alt avg `-0.094` n `230`; crypto_major avg `0.0258` n `8`; equity avg `-0.02` n `114`; fx avg `0.0012` n `6`; index avg `0.0003` n `25`; metal avg `-0.0101` n `20`; unknown avg `8.8549` n `791`
- 4h: commodity avg `0.004` n `12`; crypto_alt avg `0.4368` n `230`; crypto_major avg `0.3023` n `8`; equity avg `0.0231` n `114`; fx avg `-0.007` n `6`; index avg `0.0069` n `25`; metal avg `-0.0134` n `20`; unknown avg `10.3351` n `791`
- 24h: commodity avg `-0.0998` n `12`; crypto_alt avg `0.8115` n `230`; crypto_major avg `0.3312` n `8`; equity avg `0.2849` n `114`; fx avg `0.0256` n `6`; index avg `0.0462` n `25`; metal avg `-0.027` n `20`; unknown avg `0.0093` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
