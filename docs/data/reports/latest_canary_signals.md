# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T23:46:28.714131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `0.0992` n `228`; crypto_major avg `0.0705` n `8`; equity avg `-0.0038` n `69`; fx avg `-0.0006` n `6`; index avg `-0.0079` n `23`; metal avg `0.0004` n `18`; unknown avg `-0.1655` n `421`
- 1h: commodity avg `-0.0522` n `12`; crypto_alt avg `-0.0133` n `228`; crypto_major avg `0.058` n `8`; equity avg `0.0509` n `69`; fx avg `-0.017` n `6`; index avg `-0.0349` n `23`; metal avg `-0.0101` n `18`; unknown avg `-0.3608` n `421`
- 4h: commodity avg `0.0527` n `12`; crypto_alt avg `-0.7664` n `228`; crypto_major avg `-0.3139` n `8`; equity avg `0.165` n `69`; fx avg `-0.0191` n `6`; index avg `-0.0232` n `23`; metal avg `-0.0103` n `18`; unknown avg `-0.5179` n `421`
- 24h: commodity avg `-0.2561` n `12`; crypto_alt avg `0.8442` n `228`; crypto_major avg `2.5276` n `8`; equity avg `1.0415` n `69`; fx avg `0.0231` n `6`; index avg `0.0335` n `23`; metal avg `0.0049` n `18`; unknown avg `0.1077` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
