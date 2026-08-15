# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T15:07:06.153178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `0.0464` n `230`; crypto_major avg `0.0079` n `8`; equity avg `0.0185` n `114`; fx avg `-0.0006` n `6`; index avg `0.0024` n `25`; metal avg `-0.0039` n `20`; unknown avg `-0.0235` n `791`
- 1h: commodity avg `-0.0089` n `12`; crypto_alt avg `0.2087` n `230`; crypto_major avg `0.0199` n `8`; equity avg `0.0042` n `114`; fx avg `-0.0054` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0035` n `20`; unknown avg `-0.0793` n `791`
- 4h: commodity avg `0.0429` n `12`; crypto_alt avg `0.2331` n `230`; crypto_major avg `0.1312` n `8`; equity avg `0.0575` n `114`; fx avg `-0.0062` n `6`; index avg `0.0204` n `25`; metal avg `-0.0182` n `20`; unknown avg `-0.1329` n `791`
- 24h: commodity avg `-0.143` n `12`; crypto_alt avg `1.5599` n `230`; crypto_major avg `0.5508` n `8`; equity avg `-0.0151` n `114`; fx avg `0.0676` n `6`; index avg `-0.0327` n `25`; metal avg `-0.0206` n `20`; unknown avg `0.0231` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
