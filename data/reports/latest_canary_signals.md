# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T22:52:28.729983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5119` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.2571` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.2144` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0259` n `12`; crypto_alt avg `-1.0543` n `230`; crypto_major avg `-0.7507` n `8`; equity avg `-0.0999` n `102`; fx avg `-0.0066` n `6`; index avg `0.0017` n `25`; metal avg `-0.006` n `20`; unknown avg `-0.1491` n `774`
- 1h: commodity avg `-0.0424` n `12`; crypto_alt avg `-1.5583` n `230`; crypto_major avg `-1.2979` n `8`; equity avg `-0.4334` n `102`; fx avg `-0.0013` n `6`; index avg `-0.0408` n `25`; metal avg `-0.0358` n `20`; unknown avg `1.5317` n `774`
- 4h: commodity avg `-0.0795` n `12`; crypto_alt avg `-1.2086` n `230`; crypto_major avg `-1.1356` n `8`; equity avg `0.3763` n `102`; fx avg `-0.0257` n `6`; index avg `0.0788` n `25`; metal avg `0.0277` n `20`; unknown avg `1389.9278` n `774`
- 24h: commodity avg `-0.6561` n `12`; crypto_alt avg `-3.3828` n `230`; crypto_major avg `-2.807` n `8`; equity avg `-1.8301` n `102`; fx avg `-0.0454` n `6`; index avg `-0.4765` n `25`; metal avg `-0.0621` n `20`; unknown avg `1420.7454` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
