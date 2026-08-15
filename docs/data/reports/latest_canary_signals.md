# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T21:37:28.443934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.0178` n `230`; crypto_major avg `0.0258` n `8`; equity avg `0.0096` n `114`; fx avg `0.001` n `6`; index avg `-0.0004` n `25`; metal avg `0.0036` n `20`; unknown avg `0.1393` n `791`
- 1h: commodity avg `-0.0291` n `12`; crypto_alt avg `0.1309` n `230`; crypto_major avg `0.1137` n `8`; equity avg `-0.0032` n `114`; fx avg `-0.0003` n `6`; index avg `-0.0024` n `25`; metal avg `0.0003` n `20`; unknown avg `0.1727` n `791`
- 4h: commodity avg `0.0199` n `12`; crypto_alt avg `-0.0913` n `230`; crypto_major avg `0.0799` n `8`; equity avg `0.0695` n `114`; fx avg `0.0076` n `6`; index avg `-0.0129` n `25`; metal avg `0.0079` n `20`; unknown avg `0.9757` n `791`
- 24h: commodity avg `-0.0235` n `12`; crypto_alt avg `0.9557` n `230`; crypto_major avg `0.6731` n `8`; equity avg `0.1921` n `114`; fx avg `0.0275` n `6`; index avg `-0.0164` n `25`; metal avg `0.0221` n `20`; unknown avg `0.2143` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
