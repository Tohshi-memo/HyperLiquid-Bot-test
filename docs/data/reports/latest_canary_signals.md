# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T11:06:35.954774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0175` n `12`; crypto_alt avg `0.0143` n `230`; crypto_major avg `-0.0142` n `8`; equity avg `0.0095` n `114`; fx avg `-0.0302` n `6`; index avg `-0.001` n `25`; metal avg `0.0084` n `20`; unknown avg `0.0146` n `791`
- 1h: commodity avg `-0.0308` n `12`; crypto_alt avg `-0.0402` n `230`; crypto_major avg `0.0076` n `8`; equity avg `0.0102` n `114`; fx avg `0.0018` n `6`; index avg `0.0066` n `25`; metal avg `0.014` n `20`; unknown avg `-0.0463` n `791`
- 4h: commodity avg `-0.1343` n `12`; crypto_alt avg `-0.0321` n `230`; crypto_major avg `-0.2164` n `8`; equity avg `0.0136` n `114`; fx avg `-0.0079` n `6`; index avg `-0.0018` n `25`; metal avg `0.0095` n `20`; unknown avg `0.0003` n `791`
- 24h: commodity avg `-0.0334` n `12`; crypto_alt avg `1.1908` n `230`; crypto_major avg `0.2057` n `8`; equity avg `-0.7279` n `114`; fx avg `0.1295` n `6`; index avg `-0.1627` n `25`; metal avg `0.2453` n `20`; unknown avg `-0.142` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1828`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
