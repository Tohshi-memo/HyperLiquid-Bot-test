# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T11:22:17.036936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0256` n `12`; crypto_alt avg `-0.2152` n `228`; crypto_major avg `-0.1293` n `8`; equity avg `-0.0118` n `69`; fx avg `0.0005` n `6`; index avg `-0.014` n `23`; metal avg `-0.0052` n `18`; unknown avg `-0.1425` n `421`
- 1h: commodity avg `0.0845` n `12`; crypto_alt avg `-0.3262` n `228`; crypto_major avg `-0.1619` n `8`; equity avg `-0.0012` n `69`; fx avg `0.0092` n `6`; index avg `0.005` n `23`; metal avg `-0.0195` n `18`; unknown avg `-0.2347` n `421`
- 4h: commodity avg `0.0473` n `12`; crypto_alt avg `-0.1376` n `228`; crypto_major avg `-0.0273` n `8`; equity avg `0.0779` n `69`; fx avg `0.0204` n `6`; index avg `-0.0814` n `23`; metal avg `0.0279` n `18`; unknown avg `-0.2748` n `421`
- 24h: commodity avg `-0.1109` n `12`; crypto_alt avg `1.1001` n `228`; crypto_major avg `1.7569` n `8`; equity avg `1.2201` n `69`; fx avg `0.1129` n `6`; index avg `-0.1224` n `23`; metal avg `-0.1793` n `18`; unknown avg `0.2248` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
