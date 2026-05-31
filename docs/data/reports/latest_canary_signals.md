# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T22:22:17.902945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1292` n `12`; crypto_alt avg `0.3468` n `228`; crypto_major avg `0.2382` n `8`; equity avg `-0.0285` n `69`; fx avg `0.0065` n `6`; index avg `0.0131` n `23`; metal avg `0.241` n `18`; unknown avg `0.1328` n `421`
- 1h: commodity avg `0.646` n `12`; crypto_alt avg `0.6726` n `228`; crypto_major avg `0.3593` n `8`; equity avg `-0.0474` n `69`; fx avg `0.0011` n `6`; index avg `-0.0131` n `23`; metal avg `-0.0578` n `18`; unknown avg `0.2527` n `421`
- 4h: commodity avg `0.4486` n `12`; crypto_alt avg `1.6676` n `228`; crypto_major avg `0.987` n `8`; equity avg `0.0126` n `69`; fx avg `-0.0185` n `6`; index avg `0.1645` n `23`; metal avg `-0.0596` n `18`; unknown avg `1.021` n `421`
- 24h: commodity avg `0.972` n `12`; crypto_alt avg `0.7709` n `228`; crypto_major avg `0.5898` n `8`; equity avg `0.7842` n `69`; fx avg `-0.0355` n `6`; index avg `0.2901` n `23`; metal avg `-0.2065` n `18`; unknown avg `1.1533` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.309`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2166`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
