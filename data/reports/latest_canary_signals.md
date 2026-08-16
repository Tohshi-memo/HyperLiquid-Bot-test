# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T09:58:58.250888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `0.0335` n `230`; crypto_major avg `-0.0553` n `8`; equity avg `0.0129` n `114`; fx avg `-0.0044` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.0717` n `791`
- 1h: commodity avg `-0.0217` n `12`; crypto_alt avg `0.1218` n `230`; crypto_major avg `-0.0643` n `8`; equity avg `-0.0079` n `114`; fx avg `-0.0027` n `6`; index avg `0.002` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.0721` n `791`
- 4h: commodity avg `0.0043` n `12`; crypto_alt avg `0.4277` n `230`; crypto_major avg `0.1247` n `8`; equity avg `0.0537` n `114`; fx avg `0.0011` n `6`; index avg `0.0161` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.0071` n `759`
- 24h: commodity avg `0.092` n `12`; crypto_alt avg `0.1286` n `230`; crypto_major avg `0.1607` n `8`; equity avg `0.3861` n `114`; fx avg `-0.0128` n `6`; index avg `0.0655` n `25`; metal avg `0.0256` n `20`; unknown avg `0.0582` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2057`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
