# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T18:37:27.225256+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `0.0396` n `230`; crypto_major avg `0.0046` n `8`; equity avg `-0.0192` n `114`; fx avg `0.0078` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.045` n `791`
- 1h: commodity avg `0.0187` n `12`; crypto_alt avg `-0.1496` n `230`; crypto_major avg `-0.1973` n `8`; equity avg `-0.0045` n `114`; fx avg `0.008` n `6`; index avg `-0.011` n `25`; metal avg `-0.0036` n `20`; unknown avg `0.1462` n `791`
- 4h: commodity avg `0.0492` n `12`; crypto_alt avg `-0.1107` n `230`; crypto_major avg `0.0001` n `8`; equity avg `0.0584` n `114`; fx avg `0.0069` n `6`; index avg `-0.0144` n `25`; metal avg `0.0061` n `20`; unknown avg `0.0406` n `791`
- 24h: commodity avg `0.0462` n `12`; crypto_alt avg `-0.3027` n `230`; crypto_major avg `-0.0005` n `8`; equity avg `0.2881` n `114`; fx avg `-0.0052` n `6`; index avg `0.0137` n `25`; metal avg `0.0474` n `20`; unknown avg `0.1722` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2149`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
