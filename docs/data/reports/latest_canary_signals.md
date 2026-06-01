# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T04:22:23.894493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0516` n `12`; crypto_alt avg `-0.4217` n `228`; crypto_major avg `-0.3902` n `8`; equity avg `-0.0316` n `69`; fx avg `0.0068` n `6`; index avg `-0.0414` n `23`; metal avg `0.1014` n `18`; unknown avg `-0.0535` n `422`
- 1h: commodity avg `0.1341` n `12`; crypto_alt avg `-0.6605` n `228`; crypto_major avg `-0.6366` n `8`; equity avg `-0.0782` n `69`; fx avg `-0.0314` n `6`; index avg `0.0208` n `23`; metal avg `0.0061` n `18`; unknown avg `-0.2915` n `422`
- 4h: commodity avg `0.2551` n `12`; crypto_alt avg `-0.1037` n `228`; crypto_major avg `-0.3992` n `8`; equity avg `0.1227` n `69`; fx avg `0.048` n `6`; index avg `0.5318` n `23`; metal avg `-0.0925` n `18`; unknown avg `-0.4251` n `421`
- 24h: commodity avg `1.0768` n `12`; crypto_alt avg `0.4417` n `228`; crypto_major avg `-0.8263` n `8`; equity avg `0.5351` n `69`; fx avg `0.0167` n `6`; index avg `0.6997` n `23`; metal avg `0.1919` n `18`; unknown avg `1.7438` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2882`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2244`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2033`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
