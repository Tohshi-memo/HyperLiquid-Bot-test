# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T23:22:18.555334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `-0.3802` n `228`; crypto_major avg `-0.3333` n `8`; equity avg `-0.0384` n `69`; fx avg `-0.0018` n `6`; index avg `-0.3553` n `23`; metal avg `0.0752` n `18`; unknown avg `-0.001` n `421`
- 1h: commodity avg `-0.1619` n `12`; crypto_alt avg `0.0468` n `228`; crypto_major avg `-0.0007` n `8`; equity avg `0.0078` n `69`; fx avg `-0.0009` n `6`; index avg `-0.2171` n `23`; metal avg `0.261` n `18`; unknown avg `0.7313` n `421`
- 4h: commodity avg `0.2673` n `12`; crypto_alt avg `1.6514` n `228`; crypto_major avg `1.0078` n `8`; equity avg `0.0049` n `69`; fx avg `-0.0145` n `6`; index avg `-0.167` n `23`; metal avg `0.186` n `18`; unknown avg `1.6252` n `421`
- 24h: commodity avg `0.8909` n `12`; crypto_alt avg `1.0277` n `228`; crypto_major avg `0.5593` n `8`; equity avg `0.6116` n `69`; fx avg `-0.0207` n `6`; index avg `0.0626` n `23`; metal avg `0.084` n `18`; unknown avg `1.8774` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3539`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2502`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
