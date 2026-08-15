# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T12:07:26.791624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `0.0281` n `230`; crypto_major avg `0.0241` n `8`; equity avg `-0.0037` n `114`; fx avg `-0.0012` n `6`; index avg `0.0035` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.0062` n `791`
- 1h: commodity avg `0.0924` n `12`; crypto_alt avg `0.0231` n `230`; crypto_major avg `0.0124` n `8`; equity avg `0.0126` n `114`; fx avg `-0.0021` n `6`; index avg `0.0047` n `25`; metal avg `-0.0074` n `20`; unknown avg `-0.018` n `791`
- 4h: commodity avg `0.0998` n `12`; crypto_alt avg `0.0705` n `230`; crypto_major avg `-0.0671` n `8`; equity avg `0.0196` n `114`; fx avg `-0.0148` n `6`; index avg `0.0048` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.1611` n `791`
- 24h: commodity avg `-0.0107` n `12`; crypto_alt avg `1.1498` n `230`; crypto_major avg `0.1971` n `8`; equity avg `-0.6027` n `114`; fx avg `0.1157` n `6`; index avg `-0.1482` n `25`; metal avg `0.0777` n `20`; unknown avg `-0.1267` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
