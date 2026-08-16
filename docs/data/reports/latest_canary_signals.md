# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T07:52:37.334014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0169` n `12`; crypto_alt avg `-0.0213` n `230`; crypto_major avg `0.0204` n `8`; equity avg `0.0008` n `114`; fx avg `0.0044` n `6`; index avg `-0.0038` n `25`; metal avg `0.0024` n `20`; unknown avg `0.0084` n `791`
- 1h: commodity avg `0.0194` n `12`; crypto_alt avg `0.2635` n `230`; crypto_major avg `0.1301` n `8`; equity avg `-0.0188` n `114`; fx avg `0.012` n `6`; index avg `0.0042` n `25`; metal avg `-0.0047` n `20`; unknown avg `0.0302` n `791`
- 4h: commodity avg `-0.0222` n `12`; crypto_alt avg `0.1826` n `230`; crypto_major avg `0.004` n `8`; equity avg `0.0889` n `114`; fx avg `0.0128` n `6`; index avg `0.0197` n `25`; metal avg `0.0138` n `20`; unknown avg `-0.0109` n `759`
- 24h: commodity avg `0.1209` n `12`; crypto_alt avg `0.0923` n `230`; crypto_major avg `0.0838` n `8`; equity avg `0.3703` n `114`; fx avg `-0.001` n `6`; index avg `0.0524` n `25`; metal avg `0.0314` n `20`; unknown avg `0.0662` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2099`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
