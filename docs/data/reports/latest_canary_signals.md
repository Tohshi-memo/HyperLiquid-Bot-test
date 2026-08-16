# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T04:37:26.366237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `0.0092` n `230`; crypto_major avg `-0.038` n `8`; equity avg `-0.0109` n `114`; fx avg `0.0018` n `6`; index avg `0.0003` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.1928` n `791`
- 1h: commodity avg `0.0131` n `12`; crypto_alt avg `-0.1345` n `230`; crypto_major avg `-0.0556` n `8`; equity avg `-0.0041` n `114`; fx avg `0.0079` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0052` n `20`; unknown avg `0.1062` n `791`
- 4h: commodity avg `0.0702` n `12`; crypto_alt avg `-0.3186` n `230`; crypto_major avg `0.0518` n `8`; equity avg `0.1247` n `114`; fx avg `0.0057` n `6`; index avg `0.0048` n `25`; metal avg `0.0167` n `20`; unknown avg `-0.0376` n `791`
- 24h: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.1773` n `230`; crypto_major avg `-0.129` n `8`; equity avg `0.2303` n `114`; fx avg `-0.0121` n `6`; index avg `0.0198` n `25`; metal avg `0.0101` n `20`; unknown avg `-0.0156` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2216`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
