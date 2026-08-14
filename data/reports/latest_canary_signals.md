# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T23:52:28.043312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.0097` n `230`; crypto_major avg `0.0159` n `8`; equity avg `-0.0253` n `114`; fx avg `0.0514` n `6`; index avg `-0.0043` n `25`; metal avg `0.0055` n `20`; unknown avg `0.0858` n `791`
- 1h: commodity avg `0.0337` n `12`; crypto_alt avg `0.2053` n `230`; crypto_major avg `0.3089` n `8`; equity avg `-0.0062` n `114`; fx avg `-0.0179` n `6`; index avg `-0.0044` n `25`; metal avg `0.0331` n `20`; unknown avg `0.2206` n `791`
- 4h: commodity avg `0.0807` n `12`; crypto_alt avg `0.3638` n `230`; crypto_major avg `0.3475` n `8`; equity avg `0.0684` n `114`; fx avg `-0.0173` n `6`; index avg `0.0132` n `25`; metal avg `0.0324` n `20`; unknown avg `2.5786` n `791`
- 24h: commodity avg `0.2231` n `12`; crypto_alt avg `0.2136` n `230`; crypto_major avg `-0.6212` n `8`; equity avg `-0.5467` n `114`; fx avg `0.0676` n `6`; index avg `-0.1176` n `25`; metal avg `0.2199` n `20`; unknown avg `-0.0435` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
