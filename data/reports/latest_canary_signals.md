# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T22:37:35.758419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `12`; crypto_alt avg `-0.0087` n `230`; crypto_major avg `-0.0175` n `8`; equity avg `0.0143` n `113`; fx avg `-0.0014` n `6`; index avg `0.0004` n `25`; metal avg `0.0359` n `20`; unknown avg `-0.008` n `787`
- 1h: commodity avg `-0.0412` n `12`; crypto_alt avg `0.1218` n `230`; crypto_major avg `0.1337` n `8`; equity avg `0.0475` n `113`; fx avg `-0.0055` n `6`; index avg `0.0122` n `25`; metal avg `0.0144` n `20`; unknown avg `0.1004` n `787`
- 4h: commodity avg `-0.0022` n `12`; crypto_alt avg `0.5593` n `230`; crypto_major avg `0.5069` n `8`; equity avg `0.148` n `113`; fx avg `0.003` n `6`; index avg `0.0195` n `25`; metal avg `-0.0651` n `20`; unknown avg `0.3932` n `787`
- 24h: commodity avg `-0.4433` n `12`; crypto_alt avg `0.7691` n `230`; crypto_major avg `0.8605` n `8`; equity avg `1.8243` n `113`; fx avg `0.0199` n `6`; index avg `0.3496` n `25`; metal avg `-0.3941` n `20`; unknown avg `0.2024` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2411`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.205`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
