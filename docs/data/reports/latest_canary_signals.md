# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T12:37:28.479618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `0.2952` n `230`; crypto_major avg `0.3064` n `8`; equity avg `0.2595` n `93`; fx avg `-0.0116` n `6`; index avg `0.0649` n `25`; metal avg `0.1571` n `20`; unknown avg `0.0935` n `768`
- 1h: commodity avg `-0.017` n `12`; crypto_alt avg `0.3568` n `230`; crypto_major avg `0.2412` n `8`; equity avg `0.0847` n `93`; fx avg `-0.0039` n `6`; index avg `0.0141` n `25`; metal avg `0.1839` n `20`; unknown avg `0.0884` n `767`
- 4h: commodity avg `-0.0342` n `12`; crypto_alt avg `0.5987` n `230`; crypto_major avg `0.5035` n `8`; equity avg `0.1275` n `93`; fx avg `-0.0189` n `6`; index avg `0.0048` n `25`; metal avg `0.061` n `20`; unknown avg `-0.0445` n `767`
- 24h: commodity avg `-0.0931` n `12`; crypto_alt avg `1.0992` n `230`; crypto_major avg `2.1153` n `8`; equity avg `0.7059` n `92`; fx avg `0.0223` n `6`; index avg `0.1777` n `25`; metal avg `0.0034` n `20`; unknown avg `0.1465` n `738`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
