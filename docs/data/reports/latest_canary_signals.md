# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T05:52:23.431496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0379` n `12`; crypto_alt avg `-0.2498` n `228`; crypto_major avg `-0.0603` n `8`; equity avg `0.0034` n `69`; fx avg `0.0` n `6`; index avg `-0.0643` n `23`; metal avg `0.0036` n `18`; unknown avg `-0.581` n `421`
- 1h: commodity avg `0.0639` n `12`; crypto_alt avg `-0.246` n `228`; crypto_major avg `0.0026` n `8`; equity avg `0.0543` n `69`; fx avg `-0.0057` n `6`; index avg `0.0109` n `23`; metal avg `0.0464` n `18`; unknown avg `-0.5362` n `421`
- 4h: commodity avg `0.0749` n `12`; crypto_alt avg `0.2228` n `228`; crypto_major avg `0.3356` n `8`; equity avg `0.1818` n `69`; fx avg `0.0137` n `6`; index avg `-0.0339` n `23`; metal avg `-0.0159` n `18`; unknown avg `-0.9409` n `419`
- 24h: commodity avg `0.1297` n `12`; crypto_alt avg `0.3741` n `228`; crypto_major avg `2.3034` n `8`; equity avg `0.9257` n `69`; fx avg `0.0396` n `6`; index avg `0.0253` n `23`; metal avg `0.0067` n `18`; unknown avg `0.5237` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
