# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T13:41:03.781739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.017` n `12`; crypto_alt avg `-0.0088` n `230`; crypto_major avg `-0.0319` n `8`; equity avg `0.0025` n `114`; fx avg `0.0008` n `6`; index avg `0.0053` n `25`; metal avg `-0.0044` n `20`; unknown avg `-0.0454` n `791`
- 1h: commodity avg `-0.0231` n `12`; crypto_alt avg `0.0668` n `230`; crypto_major avg `0.0473` n `8`; equity avg `-0.0119` n `114`; fx avg `-0.0082` n `6`; index avg `0.0077` n `25`; metal avg `-0.0128` n `20`; unknown avg `0.0427` n `791`
- 4h: commodity avg `-0.0202` n `12`; crypto_alt avg `0.0345` n `230`; crypto_major avg `-0.0593` n `8`; equity avg `-0.1183` n `114`; fx avg `-0.0183` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0048` n `20`; unknown avg `0.1404` n `791`
- 24h: commodity avg `0.0405` n `12`; crypto_alt avg `0.0625` n `230`; crypto_major avg `0.0025` n `8`; equity avg `0.2516` n `114`; fx avg `-0.013` n `6`; index avg `0.0389` n `25`; metal avg `0.0262` n `20`; unknown avg `0.1026` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1663`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
