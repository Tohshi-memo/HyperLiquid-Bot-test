# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T13:07:26.617234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `0.0545` n `230`; crypto_major avg `0.1566` n `8`; equity avg `-0.0025` n `114`; fx avg `-0.0062` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0012` n `20`; unknown avg `0.0266` n `791`
- 1h: commodity avg `-0.0412` n `12`; crypto_alt avg `-0.0702` n `230`; crypto_major avg `0.1406` n `8`; equity avg `0.0001` n `114`; fx avg `-0.0023` n `6`; index avg `0.0126` n `25`; metal avg `-0.0049` n `20`; unknown avg `0.0345` n `791`
- 4h: commodity avg `0.0474` n `12`; crypto_alt avg `0.0326` n `230`; crypto_major avg `0.2655` n `8`; equity avg `0.0479` n `114`; fx avg `-0.0096` n `6`; index avg `0.0104` n `25`; metal avg `-0.005` n `20`; unknown avg `-0.0077` n `791`
- 24h: commodity avg `0.0383` n `12`; crypto_alt avg `1.0945` n `230`; crypto_major avg `0.5299` n `8`; equity avg `-0.6752` n `114`; fx avg `0.1267` n `6`; index avg `-0.1391` n `25`; metal avg `0.0536` n `20`; unknown avg `-0.0527` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1842`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
