# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T01:22:24.978782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `0.0865` n `230`; crypto_major avg `0.1173` n `8`; equity avg `0.0589` n `114`; fx avg `0.0071` n `6`; index avg `0.0029` n `25`; metal avg `0.0388` n `20`; unknown avg `-0.0594` n `792`
- 1h: commodity avg `-0.0202` n `12`; crypto_alt avg `0.5285` n `230`; crypto_major avg `0.7367` n `8`; equity avg `0.2407` n `114`; fx avg `-0.0366` n `6`; index avg `-0.0011` n `25`; metal avg `0.2179` n `20`; unknown avg `0.5684` n `792`
- 4h: commodity avg `-0.2106` n `12`; crypto_alt avg `0.0394` n `230`; crypto_major avg `0.2345` n `8`; equity avg `0.2155` n `114`; fx avg `-0.0674` n `6`; index avg `0.0263` n `25`; metal avg `0.2977` n `20`; unknown avg `-0.1811` n `791`
- 24h: commodity avg `-0.1838` n `12`; crypto_alt avg `-0.1665` n `230`; crypto_major avg `0.2216` n `8`; equity avg `0.526` n `114`; fx avg `-0.0641` n `6`; index avg `0.049` n `25`; metal avg `0.3146` n `20`; unknown avg `0.0521` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
