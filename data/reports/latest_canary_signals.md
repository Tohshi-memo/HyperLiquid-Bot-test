# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T17:37:17.432105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0689` n `12`; crypto_alt avg `0.0037` n `228`; crypto_major avg `0.0025` n `8`; equity avg `0.0142` n `67`; fx avg `-0.0081` n `6`; index avg `-0.1802` n `23`; metal avg `-0.0937` n `18`; unknown avg `0.0989` n `405`
- 1h: commodity avg `-0.4349` n `12`; crypto_alt avg `0.278` n `228`; crypto_major avg `-0.0621` n `8`; equity avg `0.0829` n `67`; fx avg `-0.0141` n `6`; index avg `0.1265` n `23`; metal avg `0.1166` n `18`; unknown avg `0.9536` n `405`
- 4h: commodity avg `-0.9091` n `12`; crypto_alt avg `1.1145` n `228`; crypto_major avg `0.0144` n `8`; equity avg `0.1524` n `67`; fx avg `-0.0289` n `6`; index avg `0.1446` n `23`; metal avg `0.5566` n `18`; unknown avg `0.9873` n `405`
- 24h: commodity avg `-1.3208` n `12`; crypto_alt avg `2.1741` n `228`; crypto_major avg `0.4275` n `8`; equity avg `0.8848` n `67`; fx avg `-0.0392` n `6`; index avg `0.6323` n `23`; metal avg `1.6161` n `18`; unknown avg `1.9703` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
