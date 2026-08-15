# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T21:52:49.349205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.0136` n `230`; crypto_major avg `-0.013` n `8`; equity avg `0.0086` n `114`; fx avg `0.0012` n `6`; index avg `0.0002` n `25`; metal avg `0.0044` n `20`; unknown avg `-0.0551` n `791`
- 1h: commodity avg `-0.0092` n `12`; crypto_alt avg `0.079` n `230`; crypto_major avg `0.0662` n `8`; equity avg `0.0132` n `114`; fx avg `0.0065` n `6`; index avg `0.0067` n `25`; metal avg `0.0039` n `20`; unknown avg `-0.0039` n `791`
- 4h: commodity avg `0.0187` n `12`; crypto_alt avg `-0.1003` n `230`; crypto_major avg `0.0548` n `8`; equity avg `0.0724` n `114`; fx avg `0.0023` n `6`; index avg `-0.016` n `25`; metal avg `0.0101` n `20`; unknown avg `0.8784` n `791`
- 24h: commodity avg `-0.0468` n `12`; crypto_alt avg `0.9943` n `230`; crypto_major avg `0.7006` n `8`; equity avg `0.187` n `114`; fx avg `0.025` n `6`; index avg `-0.0148` n `25`; metal avg `0.0184` n `20`; unknown avg `0.104` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1998`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
