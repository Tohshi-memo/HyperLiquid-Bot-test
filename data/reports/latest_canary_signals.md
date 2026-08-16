# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T21:22:33.092141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0209` n `12`; crypto_alt avg `-0.045` n `230`; crypto_major avg `-0.0131` n `8`; equity avg `-0.0032` n `114`; fx avg `0.0086` n `6`; index avg `0.0017` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.0044` n `791`
- 1h: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.4` n `230`; crypto_major avg `-0.1853` n `8`; equity avg `0.0082` n `114`; fx avg `0.007` n `6`; index avg `-0.0071` n `25`; metal avg `-0.011` n `20`; unknown avg `0.3808` n `791`
- 4h: commodity avg `0.0356` n `12`; crypto_alt avg `-0.5059` n `230`; crypto_major avg `-0.3582` n `8`; equity avg `0.0234` n `114`; fx avg `0.0094` n `6`; index avg `0.0029` n `25`; metal avg `-0.0309` n `20`; unknown avg `0.1454` n `791`
- 24h: commodity avg `0.0484` n `12`; crypto_alt avg `-0.7076` n `230`; crypto_major avg `-0.245` n `8`; equity avg `0.2932` n `114`; fx avg `0.0031` n `6`; index avg `0.0396` n `25`; metal avg `0.0252` n `20`; unknown avg `0.1488` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2197`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1706`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
