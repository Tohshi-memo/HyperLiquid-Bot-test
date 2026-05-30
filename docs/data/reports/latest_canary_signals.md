# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T20:22:15.501433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0121` n `12`; crypto_alt avg `0.0205` n `228`; crypto_major avg `-0.1366` n `8`; equity avg `0.0294` n `69`; fx avg `0.0021` n `6`; index avg `0.1355` n `23`; metal avg `-0.0011` n `18`; unknown avg `-0.1553` n `421`
- 1h: commodity avg `-0.1202` n `12`; crypto_alt avg `0.0565` n `228`; crypto_major avg `-0.1109` n `8`; equity avg `0.0427` n `69`; fx avg `0.0064` n `6`; index avg `-0.062` n `23`; metal avg `-0.0055` n `18`; unknown avg `-0.7237` n `421`
- 4h: commodity avg `0.2127` n `12`; crypto_alt avg `0.522` n `228`; crypto_major avg `0.5712` n `8`; equity avg `0.1624` n `69`; fx avg `0.0022` n `6`; index avg `0.0151` n `23`; metal avg `-0.0109` n `18`; unknown avg `-0.3753` n `421`
- 24h: commodity avg `-0.1332` n `12`; crypto_alt avg `1.5535` n `228`; crypto_major avg `2.4386` n `8`; equity avg `0.942` n `69`; fx avg `-0.0246` n `6`; index avg `0.0028` n `23`; metal avg `-0.046` n `18`; unknown avg `0.2966` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
