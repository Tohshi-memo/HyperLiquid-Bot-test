# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T17:53:18.448056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.0427` n `230`; crypto_major avg `-0.1675` n `8`; equity avg `-0.0559` n `114`; fx avg `-0.0103` n `6`; index avg `-0.0055` n `25`; metal avg `-0.0364` n `20`; unknown avg `1.7767` n `791`
- 1h: commodity avg `0.0409` n `12`; crypto_alt avg `0.0344` n `230`; crypto_major avg `-0.1221` n `8`; equity avg `0.0332` n `114`; fx avg `-0.0146` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0648` n `20`; unknown avg `0.3065` n `791`
- 4h: commodity avg `0.2165` n `12`; crypto_alt avg `0.5968` n `230`; crypto_major avg `0.2114` n `8`; equity avg `-0.7823` n `114`; fx avg `0.0424` n `6`; index avg `-0.1491` n `25`; metal avg `-0.0364` n `20`; unknown avg `37.7932` n `786`
- 24h: commodity avg `0.1573` n `12`; crypto_alt avg `0.5041` n `230`; crypto_major avg `-0.6022` n `8`; equity avg `-0.6639` n `114`; fx avg `0.0673` n `6`; index avg `-0.1312` n `25`; metal avg `0.1046` n `20`; unknown avg `0.1345` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
