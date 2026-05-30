# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T17:07:21.202380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.0704` n `228`; crypto_major avg `0.0791` n `8`; equity avg `0.0146` n `69`; fx avg `-0.0345` n `6`; index avg `0.0098` n `23`; metal avg `0.0117` n `18`; unknown avg `0.0505` n `421`
- 1h: commodity avg `0.5378` n `12`; crypto_alt avg `-0.0113` n `228`; crypto_major avg `0.1771` n `8`; equity avg `-0.0926` n `69`; fx avg `-0.0353` n `6`; index avg `0.0332` n `23`; metal avg `0.0057` n `18`; unknown avg `0.9035` n `421`
- 4h: commodity avg `-0.2903` n `12`; crypto_alt avg `0.0381` n `228`; crypto_major avg `0.6723` n `8`; equity avg `-0.0339` n `69`; fx avg `-0.0386` n `6`; index avg `-0.0655` n `23`; metal avg `0.0325` n `18`; unknown avg `0.3468` n `421`
- 24h: commodity avg `0.1319` n `12`; crypto_alt avg `0.6736` n `228`; crypto_major avg `1.5351` n `8`; equity avg `0.7003` n `69`; fx avg `-0.0315` n `6`; index avg `-0.0202` n `23`; metal avg `-0.2212` n `18`; unknown avg `1.1364` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1913`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
