# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T19:07:30.397053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.022` n `12`; crypto_alt avg `0.0165` n `230`; crypto_major avg `0.0318` n `8`; equity avg `0.0029` n `114`; fx avg `0.0021` n `6`; index avg `0.0043` n `25`; metal avg `-0.0009` n `20`; unknown avg `0.0024` n `791`
- 1h: commodity avg `0.0454` n `12`; crypto_alt avg `-0.0463` n `230`; crypto_major avg `-0.0897` n `8`; equity avg `0.0176` n `114`; fx avg `0.0024` n `6`; index avg `0.0035` n `25`; metal avg `0.0004` n `20`; unknown avg `0.4941` n `791`
- 4h: commodity avg `0.078` n `12`; crypto_alt avg `0.0647` n `230`; crypto_major avg `0.119` n `8`; equity avg `0.0492` n `114`; fx avg `0.0003` n `6`; index avg `0.0083` n `25`; metal avg `0.0023` n `20`; unknown avg `5.7173` n `791`
- 24h: commodity avg `-0.012` n `12`; crypto_alt avg `1.1467` n `230`; crypto_major avg `0.7404` n `8`; equity avg `0.4788` n `114`; fx avg `0.0305` n `6`; index avg `0.0371` n `25`; metal avg `0.0615` n `20`; unknown avg `0.0935` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
