# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T21:22:30.801350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0203` n `12`; crypto_alt avg `-0.122` n `230`; crypto_major avg `-0.0277` n `8`; equity avg `-0.0147` n `114`; fx avg `-0.0092` n `6`; index avg `0.0071` n `25`; metal avg `0.0147` n `20`; unknown avg `-0.0399` n `791`
- 1h: commodity avg `0.0116` n `12`; crypto_alt avg `-0.0378` n `230`; crypto_major avg `-0.0204` n `8`; equity avg `0.0027` n `114`; fx avg `-0.0139` n `6`; index avg `-0.0016` n `25`; metal avg `0.0366` n `20`; unknown avg `-0.0171` n `791`
- 4h: commodity avg `-0.0694` n `12`; crypto_alt avg `-0.2836` n `230`; crypto_major avg `-0.3807` n `8`; equity avg `0.0174` n `114`; fx avg `0.0177` n `6`; index avg `0.0314` n `25`; metal avg `-0.0235` n `20`; unknown avg `-0.3594` n `791`
- 24h: commodity avg `0.1724` n `12`; crypto_alt avg `0.107` n `230`; crypto_major avg `-1.0256` n `8`; equity avg `-0.5001` n `114`; fx avg `0.0802` n `6`; index avg `-0.0833` n `25`; metal avg `0.2126` n `20`; unknown avg `-0.0776` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1883`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1554`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
