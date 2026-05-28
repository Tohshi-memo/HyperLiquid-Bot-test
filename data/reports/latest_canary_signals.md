# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T20:07:21.477623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2384` n `12`; crypto_alt avg `-0.5217` n `228`; crypto_major avg `-0.5055` n `8`; equity avg `-0.1154` n `69`; fx avg `-0.0074` n `6`; index avg `-0.0918` n `23`; metal avg `-0.0093` n `18`; unknown avg `0.0014` n `417`
- 1h: commodity avg `0.05` n `12`; crypto_alt avg `-0.7508` n `228`; crypto_major avg `-0.5397` n `8`; equity avg `-0.0208` n `69`; fx avg `-0.0101` n `6`; index avg `-0.1228` n `23`; metal avg `-0.0696` n `18`; unknown avg `-0.0807` n `417`
- 4h: commodity avg `-0.1167` n `12`; crypto_alt avg `1.2362` n `228`; crypto_major avg `1.2621` n `8`; equity avg `0.6693` n `69`; fx avg `-0.0183` n `6`; index avg `0.1417` n `23`; metal avg `0.3493` n `18`; unknown avg `0.5005` n `417`
- 24h: commodity avg `1.153` n `12`; crypto_alt avg `-4.1593` n `228`; crypto_major avg `-1.7365` n `8`; equity avg `1.5684` n `69`; fx avg `-0.0335` n `6`; index avg `0.865` n `23`; metal avg `0.5213` n `18`; unknown avg `-0.7565` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
