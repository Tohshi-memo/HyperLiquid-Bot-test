# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T17:32:28.395110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `-0.0149` n `230`; crypto_major avg `-0.0224` n `8`; equity avg `0.0348` n `114`; fx avg `0.0` n `6`; index avg `0.0045` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0686` n `791`
- 1h: commodity avg `0.0258` n `12`; crypto_alt avg `0.1205` n `230`; crypto_major avg `0.0598` n `8`; equity avg `0.024` n `114`; fx avg `-0.004` n `6`; index avg `0.0017` n `25`; metal avg `0.0` n `20`; unknown avg `1.5218` n `791`
- 4h: commodity avg `0.0268` n `12`; crypto_alt avg `0.4288` n `230`; crypto_major avg `0.1113` n `8`; equity avg `0.0518` n `114`; fx avg `-0.0045` n `6`; index avg `0.0052` n `25`; metal avg `-0.0102` n `20`; unknown avg `0.0459` n `791`
- 24h: commodity avg `-0.1346` n `12`; crypto_alt avg `0.8501` n `230`; crypto_major avg `0.2665` n `8`; equity avg `0.2241` n `114`; fx avg `0.0241` n `6`; index avg `0.0428` n `25`; metal avg `0.0044` n `20`; unknown avg `0.0589` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
