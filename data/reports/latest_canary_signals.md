# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T16:52:34.310006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1534` n `12`; crypto_alt avg `0.4049` n `228`; crypto_major avg `0.3869` n `8`; equity avg `0.0539` n `74`; fx avg `-0.0132` n `6`; index avg `-0.0104` n `23`; metal avg `0.0383` n `18`; unknown avg `0.1327` n `424`
- 1h: commodity avg `-0.2627` n `12`; crypto_alt avg `0.1705` n `228`; crypto_major avg `0.311` n `8`; equity avg `0.2818` n `74`; fx avg `-0.0117` n `6`; index avg `0.1902` n `23`; metal avg `0.0746` n `18`; unknown avg `0.1951` n `424`
- 4h: commodity avg `-0.166` n `12`; crypto_alt avg `0.692` n `228`; crypto_major avg `0.0012` n `8`; equity avg `0.9064` n `74`; fx avg `-0.0416` n `6`; index avg `0.7011` n `23`; metal avg `-0.3529` n `18`; unknown avg `0.1067` n `424`
- 24h: commodity avg `-0.8716` n `12`; crypto_alt avg `-4.5223` n `228`; crypto_major avg `-3.197` n `8`; equity avg `-0.8953` n `73`; fx avg `0.0728` n `6`; index avg `-0.0565` n `23`; metal avg `0.6899` n `18`; unknown avg `-1.0865` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
