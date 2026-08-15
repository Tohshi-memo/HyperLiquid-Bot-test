# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T23:52:28.348170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `0.0178` n `230`; crypto_major avg `-0.0213` n `8`; equity avg `-0.0046` n `114`; fx avg `0.0006` n `6`; index avg `0.0004` n `25`; metal avg `0.0014` n `20`; unknown avg `-0.0106` n `791`
- 1h: commodity avg `0.0159` n `12`; crypto_alt avg `-0.284` n `230`; crypto_major avg `-0.188` n `8`; equity avg `0.0212` n `114`; fx avg `-0.0037` n `6`; index avg `0.0121` n `25`; metal avg `0.0033` n `20`; unknown avg `0.1659` n `791`
- 4h: commodity avg `-0.0792` n `12`; crypto_alt avg `-0.501` n `230`; crypto_major avg `-0.3071` n `8`; equity avg `-0.0086` n `114`; fx avg `-0.0016` n `6`; index avg `0.0053` n `25`; metal avg `-0.0083` n `20`; unknown avg `0.2099` n `791`
- 24h: commodity avg `-0.105` n `12`; crypto_alt avg `0.1691` n `230`; crypto_major avg `0.0342` n `8`; equity avg `0.1735` n `114`; fx avg `0.0341` n `6`; index avg `0.0115` n `25`; metal avg `-0.0159` n `20`; unknown avg `0.0559` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2215`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
