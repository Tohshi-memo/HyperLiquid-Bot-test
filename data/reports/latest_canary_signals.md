# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T04:07:23.090243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0659` n `12`; crypto_alt avg `-0.1896` n `228`; crypto_major avg `-0.1886` n `8`; equity avg `0.0328` n `69`; fx avg `-0.0261` n `6`; index avg `0.0288` n `23`; metal avg `0.0824` n `18`; unknown avg `-0.3092` n `422`
- 1h: commodity avg `0.0518` n `12`; crypto_alt avg `-0.3233` n `228`; crypto_major avg `-0.2969` n `8`; equity avg `-0.0856` n `69`; fx avg `-0.0326` n `6`; index avg `0.0566` n `23`; metal avg `-0.1641` n `18`; unknown avg `-0.334` n `422`
- 4h: commodity avg `0.3491` n `12`; crypto_alt avg `0.5525` n `228`; crypto_major avg `0.0341` n `8`; equity avg `0.2661` n `69`; fx avg `0.0572` n `6`; index avg `0.476` n `23`; metal avg `-0.2115` n `18`; unknown avg `-0.4015` n `421`
- 24h: commodity avg `1.1299` n `12`; crypto_alt avg `1.0304` n `228`; crypto_major avg `-0.2306` n `8`; equity avg `0.5443` n `69`; fx avg `0.0126` n `6`; index avg `0.7341` n `23`; metal avg `0.0893` n `18`; unknown avg `1.6741` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2881`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2244`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2032`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
