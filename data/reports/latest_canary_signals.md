# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T06:21:05.169109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `-0.158` n `230`; crypto_major avg `-0.0941` n `8`; equity avg `0.0086` n `114`; fx avg `0.0012` n `6`; index avg `-0.0001` n `25`; metal avg `0.0065` n `20`; unknown avg `1.5578` n `791`
- 1h: commodity avg `0.0062` n `12`; crypto_alt avg `-0.0533` n `230`; crypto_major avg `-0.104` n `8`; equity avg `0.0819` n `114`; fx avg `-0.0054` n `6`; index avg `0.004` n `25`; metal avg `0.0227` n `20`; unknown avg `-0.013` n `759`
- 4h: commodity avg `-0.0509` n `12`; crypto_alt avg `-0.0745` n `230`; crypto_major avg `-0.205` n `8`; equity avg `0.2069` n `114`; fx avg `-0.0033` n `6`; index avg `0.0156` n `25`; metal avg `0.033` n `20`; unknown avg `-0.0239` n `759`
- 24h: commodity avg `-0.0936` n `12`; crypto_alt avg `-0.4196` n `230`; crypto_major avg `-0.1687` n `8`; equity avg `0.4189` n `114`; fx avg `-0.0152` n `6`; index avg `0.0547` n `25`; metal avg `0.0505` n `20`; unknown avg `0.0406` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2161`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1711`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1705`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
