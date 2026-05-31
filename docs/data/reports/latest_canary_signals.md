# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T09:36:19.830264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0264` n `12`; crypto_alt avg `0.046` n `228`; crypto_major avg `-0.0285` n `8`; equity avg `-0.0074` n `69`; fx avg `0.0006` n `6`; index avg `0.0026` n `23`; metal avg `-0.0074` n `18`; unknown avg `-0.4398` n `421`
- 1h: commodity avg `0.0242` n `12`; crypto_alt avg `0.0772` n `228`; crypto_major avg `-0.0594` n `8`; equity avg `0.0049` n `69`; fx avg `-0.0068` n `6`; index avg `-0.0447` n `23`; metal avg `-0.0048` n `18`; unknown avg `-0.2847` n `421`
- 4h: commodity avg `0.153` n `12`; crypto_alt avg `-0.5742` n `228`; crypto_major avg `-0.6808` n `8`; equity avg `0.2876` n `69`; fx avg `0.0006` n `6`; index avg `-0.1641` n `23`; metal avg `-0.0262` n `18`; unknown avg `-0.224` n `401`
- 24h: commodity avg `0.2948` n `12`; crypto_alt avg `0.1805` n `228`; crypto_major avg `1.4853` n `8`; equity avg `1.1255` n `69`; fx avg `0.0142` n `6`; index avg `-0.0777` n `23`; metal avg `-0.0837` n `18`; unknown avg `0.6387` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
