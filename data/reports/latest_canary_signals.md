# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T01:37:19.483978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0164` n `12`; crypto_alt avg `-0.5964` n `228`; crypto_major avg `-0.4907` n `8`; equity avg `0.0025` n `69`; fx avg `0.0255` n `6`; index avg `0.0036` n `23`; metal avg `-0.0503` n `18`; unknown avg `-0.0763` n `422`
- 1h: commodity avg `-0.0716` n `12`; crypto_alt avg `-0.9243` n `228`; crypto_major avg `-0.9431` n `8`; equity avg `-0.1693` n `69`; fx avg `0.0233` n `6`; index avg `-0.1475` n `23`; metal avg `0.2115` n `18`; unknown avg `-0.2982` n `422`
- 4h: commodity avg `-0.2665` n `12`; crypto_alt avg `-0.774` n `228`; crypto_major avg `-0.3675` n `8`; equity avg `-0.6435` n `69`; fx avg `0.0227` n `6`; index avg `-0.4013` n `23`; metal avg `0.3964` n `18`; unknown avg `0.0058` n `422`
- 24h: commodity avg `-0.4914` n `12`; crypto_alt avg `-1.0923` n `228`; crypto_major avg `-1.6355` n `8`; equity avg `-0.7521` n `69`; fx avg `0.008` n `6`; index avg `-0.4252` n `23`; metal avg `0.0315` n `18`; unknown avg `1.4826` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
