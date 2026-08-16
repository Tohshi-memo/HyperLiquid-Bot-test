# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T15:22:26.045050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0128` n `12`; crypto_alt avg `0.0375` n `230`; crypto_major avg `0.0256` n `8`; equity avg `0.0195` n `114`; fx avg `0.0135` n `6`; index avg `-0.0031` n `25`; metal avg `0.0086` n `20`; unknown avg `-0.0516` n `791`
- 1h: commodity avg `0.013` n `12`; crypto_alt avg `-0.0245` n `230`; crypto_major avg `0.0609` n `8`; equity avg `0.0338` n `114`; fx avg `0.0253` n `6`; index avg `-0.0076` n `25`; metal avg `-0.0038` n `20`; unknown avg `-0.0267` n `791`
- 4h: commodity avg `0.0059` n `12`; crypto_alt avg `0.1295` n `230`; crypto_major avg `0.1263` n `8`; equity avg `0.009` n `114`; fx avg `-0.0088` n `6`; index avg `-0.006` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.0057` n `791`
- 24h: commodity avg `0.0705` n `12`; crypto_alt avg `-0.0937` n `230`; crypto_major avg `0.1279` n `8`; equity avg `0.2679` n `114`; fx avg `-0.0035` n `6`; index avg `0.0249` n `25`; metal avg `0.0353` n `20`; unknown avg `0.116` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2153`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1854`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
