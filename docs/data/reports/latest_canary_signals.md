# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T10:37:19.706828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `-0.0342` n `228`; crypto_major avg `-0.0321` n `8`; equity avg `0.0127` n `69`; fx avg `0.0112` n `6`; index avg `0.008` n `23`; metal avg `-0.0078` n `18`; unknown avg `0.0254` n `421`
- 1h: commodity avg `0.0516` n `12`; crypto_alt avg `0.0023` n `228`; crypto_major avg `0.0597` n `8`; equity avg `0.0241` n `69`; fx avg `-0.0047` n `6`; index avg `0.0013` n `23`; metal avg `0.0015` n `18`; unknown avg `0.0409` n `421`
- 4h: commodity avg `-0.013` n `12`; crypto_alt avg `-0.1989` n `228`; crypto_major avg `0.1636` n `8`; equity avg `0.0846` n `69`; fx avg `0.0229` n `6`; index avg `-0.0383` n `23`; metal avg `0.046` n `18`; unknown avg `-0.16` n `421`
- 24h: commodity avg `-0.1736` n `12`; crypto_alt avg `1.5047` n `228`; crypto_major avg `1.788` n `8`; equity avg `1.1174` n `69`; fx avg `0.1044` n `6`; index avg `0.0436` n `23`; metal avg `-0.2141` n `18`; unknown avg `0.5094` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
