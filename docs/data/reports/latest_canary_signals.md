# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T12:55:44.526422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `-0.086` n `228`; crypto_major avg `-0.072` n `8`; equity avg `0.0084` n `69`; fx avg `0.0` n `6`; index avg `-0.0238` n `23`; metal avg `-0.0068` n `18`; unknown avg `0.0312` n `421`
- 1h: commodity avg `-0.0101` n `12`; crypto_alt avg `0.1294` n `228`; crypto_major avg `0.069` n `8`; equity avg `0.0566` n `69`; fx avg `0.01` n `6`; index avg `0.0108` n `23`; metal avg `0.0171` n `18`; unknown avg `-0.1543` n `421`
- 4h: commodity avg `0.1008` n `12`; crypto_alt avg `0.2803` n `228`; crypto_major avg `-0.0956` n `8`; equity avg `-0.0101` n `69`; fx avg `-0.0146` n `6`; index avg `-0.0856` n `23`; metal avg `-0.0117` n `18`; unknown avg `-0.3191` n `421`
- 24h: commodity avg `0.1606` n `12`; crypto_alt avg `0.297` n `228`; crypto_major avg `1.1747` n `8`; equity avg `0.9342` n `69`; fx avg `-0.0093` n `6`; index avg `-0.1864` n `23`; metal avg `-0.0556` n `18`; unknown avg `0.5662` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
