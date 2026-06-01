# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T02:22:23.279655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0514` n `12`; crypto_alt avg `0.1568` n `228`; crypto_major avg `0.2054` n `8`; equity avg `0.0398` n `69`; fx avg `0.0187` n `6`; index avg `-0.1112` n `23`; metal avg `0.0112` n `18`; unknown avg `0.0255` n `422`
- 1h: commodity avg `0.0125` n `12`; crypto_alt avg `-0.1667` n `228`; crypto_major avg `-0.294` n `8`; equity avg `0.1285` n `69`; fx avg `0.0245` n `6`; index avg `-0.2081` n `23`; metal avg `0.2175` n `18`; unknown avg `1.0217` n `421`
- 4h: commodity avg `0.0717` n `12`; crypto_alt avg `0.1958` n `228`; crypto_major avg `-0.2428` n `8`; equity avg `0.038` n `69`; fx avg `0.0865` n `6`; index avg `-0.1566` n `23`; metal avg `0.6072` n `18`; unknown avg `1.4218` n `421`
- 24h: commodity avg `1.0624` n `12`; crypto_alt avg `0.2257` n `228`; crypto_major avg `-0.5823` n `8`; equity avg `0.5297` n `69`; fx avg `0.0411` n `6`; index avg `0.1233` n `23`; metal avg `0.469` n `18`; unknown avg `1.6631` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2836`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2549`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2046`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
