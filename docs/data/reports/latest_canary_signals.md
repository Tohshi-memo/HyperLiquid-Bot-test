# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T02:07:26.181265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.0514` n `230`; crypto_major avg `-0.0218` n `8`; equity avg `0.0289` n `114`; fx avg `-0.005` n `6`; index avg `-0.0002` n `25`; metal avg `0.0018` n `20`; unknown avg `0.0426` n `791`
- 1h: commodity avg `0.0573` n `12`; crypto_alt avg `-0.2335` n `230`; crypto_major avg `-0.0535` n `8`; equity avg `0.0332` n `114`; fx avg `-0.0001` n `6`; index avg `0.001` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.0729` n `791`
- 4h: commodity avg `0.0724` n `12`; crypto_alt avg `-0.7132` n `230`; crypto_major avg `-0.2893` n `8`; equity avg `0.019` n `114`; fx avg `-0.0043` n `6`; index avg `0.015` n `25`; metal avg `0.0031` n `20`; unknown avg `0.0298` n `791`
- 24h: commodity avg `-0.0116` n `12`; crypto_alt avg `-0.1317` n `230`; crypto_major avg `-0.0733` n `8`; equity avg `0.1736` n `114`; fx avg `0.0426` n `6`; index avg `0.0111` n `25`; metal avg `-0.0191` n `20`; unknown avg `0.0434` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2225`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1709`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
