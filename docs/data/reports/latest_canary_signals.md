# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T12:52:15.701726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `-0.0134` n `228`; crypto_major avg `0.0099` n `8`; equity avg `0.0184` n `69`; fx avg `0.0` n `6`; index avg `-0.0257` n `23`; metal avg `-0.0073` n `18`; unknown avg `0.0471` n `421`
- 1h: commodity avg `-0.0228` n `12`; crypto_alt avg `0.2021` n `228`; crypto_major avg `0.1511` n `8`; equity avg `0.0666` n `69`; fx avg `0.01` n `6`; index avg `0.0089` n `23`; metal avg `0.0165` n `18`; unknown avg `-0.1396` n `421`
- 4h: commodity avg `0.0882` n `12`; crypto_alt avg `0.3535` n `228`; crypto_major avg `-0.0139` n `8`; equity avg `-0.0001` n `69`; fx avg `-0.0146` n `6`; index avg `-0.0875` n `23`; metal avg `-0.0122` n `18`; unknown avg `-0.3038` n `421`
- 24h: commodity avg `0.1479` n `12`; crypto_alt avg `0.3701` n `228`; crypto_major avg `1.2577` n `8`; equity avg `0.9443` n `69`; fx avg `-0.0093` n `6`; index avg `-0.1883` n `23`; metal avg `-0.0562` n `18`; unknown avg `0.5812` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
