# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T09:32:10.939341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `0.1399` n `228`; crypto_major avg `0.0517` n `8`; equity avg `-0.0012` n `69`; fx avg `0.0153` n `6`; index avg `-0.0264` n `23`; metal avg `0.0223` n `18`; unknown avg `0.7856` n `421`
- 1h: commodity avg `-0.0285` n `12`; crypto_alt avg `0.1054` n `228`; crypto_major avg `0.1128` n `8`; equity avg `0.0605` n `69`; fx avg `0.203` n `6`; index avg `0.0275` n `23`; metal avg `0.0996` n `18`; unknown avg `0.8331` n `421`
- 4h: commodity avg `-0.0703` n `12`; crypto_alt avg `-0.0172` n `228`; crypto_major avg `0.241` n `8`; equity avg `0.083` n `69`; fx avg `0.0252` n `6`; index avg `0.0358` n `23`; metal avg `0.0446` n `18`; unknown avg `-0.2301` n `401`
- 24h: commodity avg `-0.23` n `12`; crypto_alt avg `1.0781` n `228`; crypto_major avg `1.5911` n `8`; equity avg `1.0101` n `69`; fx avg `0.1161` n `6`; index avg `0.0445` n `23`; metal avg `-0.0067` n `18`; unknown avg `0.1814` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1934`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
