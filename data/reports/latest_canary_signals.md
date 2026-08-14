# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T22:07:31.485434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.032` n `12`; crypto_alt avg `0.1144` n `230`; crypto_major avg `0.1195` n `8`; equity avg `0.0238` n `114`; fx avg `0.0087` n `6`; index avg `-0.0037` n `25`; metal avg `0.0061` n `20`; unknown avg `0.0758` n `791`
- 1h: commodity avg `0.0716` n `12`; crypto_alt avg `-0.0087` n `230`; crypto_major avg `0.0601` n `8`; equity avg `0.0462` n `114`; fx avg `-0.0037` n `6`; index avg `0.01` n `25`; metal avg `0.0266` n `20`; unknown avg `0.1337` n `791`
- 4h: commodity avg `0.0154` n `12`; crypto_alt avg `-0.0771` n `230`; crypto_major avg `0.0445` n `8`; equity avg `0.1601` n `114`; fx avg `0.0218` n `6`; index avg `0.0347` n `25`; metal avg `0.0318` n `20`; unknown avg `7.5087` n `791`
- 24h: commodity avg `0.2444` n `12`; crypto_alt avg `0.1166` n `230`; crypto_major avg `-0.9867` n `8`; equity avg `-0.5254` n `114`; fx avg `0.0876` n `6`; index avg `-0.0874` n `25`; metal avg `0.2602` n `20`; unknown avg `-0.0664` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
