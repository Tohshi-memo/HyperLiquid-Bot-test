# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T05:52:30.636698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `12`; crypto_alt avg `0.168` n `230`; crypto_major avg `0.0575` n `8`; equity avg `0.0608` n `102`; fx avg `-0.001` n `6`; index avg `0.0379` n `25`; metal avg `0.0554` n `20`; unknown avg `0.0075` n `774`
- 1h: commodity avg `0.0812` n `12`; crypto_alt avg `0.1378` n `230`; crypto_major avg `-0.0324` n `8`; equity avg `-0.222` n `102`; fx avg `-0.038` n `6`; index avg `-0.0449` n `25`; metal avg `-0.0582` n `20`; unknown avg `-0.2564` n `774`
- 4h: commodity avg `-0.003` n `12`; crypto_alt avg `0.5023` n `230`; crypto_major avg `0.1188` n `8`; equity avg `-0.469` n `102`; fx avg `-0.0862` n `6`; index avg `-0.0943` n `25`; metal avg `-0.042` n `20`; unknown avg `1.6971` n `774`
- 24h: commodity avg `-0.6328` n `12`; crypto_alt avg `-3.7432` n `230`; crypto_major avg `-3.4788` n `8`; equity avg `-3.8579` n `102`; fx avg `-0.1607` n `6`; index avg `-0.8499` n `25`; metal avg `-0.3597` n `20`; unknown avg `1161.8193` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
