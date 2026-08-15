# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T22:52:26.346481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.0594` n `230`; crypto_major avg `0.0059` n `8`; equity avg `-0.0112` n `114`; fx avg `0.0042` n `6`; index avg `0.0045` n `25`; metal avg `-0.006` n `20`; unknown avg `0.0363` n `791`
- 1h: commodity avg `-0.0191` n `12`; crypto_alt avg `-0.1293` n `230`; crypto_major avg `-0.0698` n `8`; equity avg `-0.0205` n `114`; fx avg `-0.0019` n `6`; index avg `0.0045` n `25`; metal avg `-0.0106` n `20`; unknown avg `0.1453` n `791`
- 4h: commodity avg `-0.0236` n `12`; crypto_alt avg `-0.1088` n `230`; crypto_major avg `0.0778` n `8`; equity avg `0.0289` n `114`; fx avg `0.0045` n `6`; index avg `-0.0041` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.0217` n `791`
- 24h: commodity avg `-0.0878` n `12`; crypto_alt avg `0.7215` n `230`; crypto_major avg `0.5473` n `8`; equity avg `0.1568` n `114`; fx avg `0.0199` n `6`; index avg `-0.0052` n `25`; metal avg `0.0136` n `20`; unknown avg `0.0786` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1979`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
