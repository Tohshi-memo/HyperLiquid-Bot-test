# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T20:37:24.123529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0354` n `12`; crypto_alt avg `-0.0272` n `230`; crypto_major avg `-0.045` n `8`; equity avg `-0.0074` n `114`; fx avg `0.0001` n `6`; index avg `0.0029` n `25`; metal avg `-0.0096` n `20`; unknown avg `0.0125` n `791`
- 1h: commodity avg `0.0025` n `12`; crypto_alt avg `-0.0635` n `230`; crypto_major avg `-0.1522` n `8`; equity avg `-0.0066` n `114`; fx avg `0.0056` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0308` n `20`; unknown avg `0.1639` n `791`
- 4h: commodity avg `0.0832` n `12`; crypto_alt avg `-0.278` n `230`; crypto_major avg `-0.2689` n `8`; equity avg `0.0199` n `114`; fx avg `-0.0012` n `6`; index avg `0.0062` n `25`; metal avg `-0.017` n `20`; unknown avg `0.1538` n `791`
- 24h: commodity avg `0.0557` n `12`; crypto_alt avg `-0.1911` n `230`; crypto_major avg `-0.017` n `8`; equity avg `0.2645` n `114`; fx avg `-0.0051` n `6`; index avg `0.0476` n `25`; metal avg `0.0232` n `20`; unknown avg `0.1614` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2182`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
