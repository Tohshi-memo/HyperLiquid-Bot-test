# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T07:50:08.573044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `-0.0367` n `230`; crypto_major avg `0.0145` n `8`; equity avg `0.0016` n `114`; fx avg `0.0044` n `6`; index avg `-0.0027` n `25`; metal avg `0.0026` n `20`; unknown avg `0.0085` n `791`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `0.2481` n `230`; crypto_major avg `0.1241` n `8`; equity avg `-0.0179` n `114`; fx avg `0.012` n `6`; index avg `0.0052` n `25`; metal avg `-0.0046` n `20`; unknown avg `0.0285` n `791`
- 4h: commodity avg `-0.0207` n `12`; crypto_alt avg `0.1673` n `230`; crypto_major avg `-0.002` n `8`; equity avg `0.0898` n `114`; fx avg `0.0128` n `6`; index avg `0.0208` n `25`; metal avg `0.0139` n `20`; unknown avg `-0.0136` n `759`
- 24h: commodity avg `0.1224` n `12`; crypto_alt avg `0.0768` n `230`; crypto_major avg `0.0777` n `8`; equity avg `0.3712` n `114`; fx avg `-0.001` n `6`; index avg `0.0535` n `25`; metal avg `0.0315` n `20`; unknown avg `0.0635` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2099`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1742`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
