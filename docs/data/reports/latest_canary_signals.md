# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T01:37:27.991770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `-0.0654` n `230`; crypto_major avg `-0.0605` n `8`; equity avg `-0.186` n `114`; fx avg `0.0168` n `6`; index avg `-0.013` n `25`; metal avg `0.0047` n `20`; unknown avg `0.0034` n `793`
- 1h: commodity avg `0.0271` n `12`; crypto_alt avg `-0.0566` n `230`; crypto_major avg `-0.1421` n `8`; equity avg `-0.3977` n `114`; fx avg `-0.0066` n `6`; index avg `-0.0589` n `25`; metal avg `-0.0729` n `20`; unknown avg `0.0467` n `793`
- 4h: commodity avg `0.0113` n `12`; crypto_alt avg `-0.4049` n `230`; crypto_major avg `0.0228` n `8`; equity avg `-0.0983` n `114`; fx avg `-0.0358` n `6`; index avg `-0.0265` n `25`; metal avg `0.0619` n `20`; unknown avg `-0.2179` n `792`
- 24h: commodity avg `0.5534` n `12`; crypto_alt avg `-0.1634` n `230`; crypto_major avg `0.6853` n `8`; equity avg `0.8697` n `114`; fx avg `0.0326` n `6`; index avg `0.0232` n `25`; metal avg `0.0601` n `20`; unknown avg `0.2776` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2315`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
