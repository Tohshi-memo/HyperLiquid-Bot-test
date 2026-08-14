# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T20:22:29.552443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.034` n `12`; crypto_alt avg `-0.0097` n `230`; crypto_major avg `-0.0366` n `8`; equity avg `0.0024` n `114`; fx avg `0.0167` n `6`; index avg `0.0059` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.0652` n `791`
- 1h: commodity avg `-0.0118` n `12`; crypto_alt avg `0.1767` n `230`; crypto_major avg `0.1158` n `8`; equity avg `0.2665` n `114`; fx avg `0.0181` n `6`; index avg `0.0314` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.0023` n `791`
- 4h: commodity avg `-0.0087` n `12`; crypto_alt avg `-0.0136` n `230`; crypto_major avg `-0.2405` n `8`; equity avg `0.0371` n `114`; fx avg `0.007` n `6`; index avg `0.032` n `25`; metal avg `-0.095` n `20`; unknown avg `18.308` n `791`
- 24h: commodity avg `0.1817` n `12`; crypto_alt avg `0.3037` n `230`; crypto_major avg `-1.0087` n `8`; equity avg `-0.3544` n `114`; fx avg `0.094` n `6`; index avg `-0.0592` n `25`; metal avg `0.2093` n `20`; unknown avg `-0.0296` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1871`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
