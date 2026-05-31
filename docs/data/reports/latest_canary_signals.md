# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T11:20:04.237972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0615` n `12`; crypto_alt avg `-0.1222` n `228`; crypto_major avg `-0.0219` n `8`; equity avg `-0.0019` n `69`; fx avg `0.0043` n `6`; index avg `-0.0276` n `23`; metal avg `-0.006` n `18`; unknown avg `-0.0547` n `421`
- 1h: commodity avg `0.0707` n `12`; crypto_alt avg `0.4155` n `228`; crypto_major avg `0.0455` n `8`; equity avg `0.0072` n `69`; fx avg `-0.0205` n `6`; index avg `-0.0382` n `23`; metal avg `-0.0056` n `18`; unknown avg `-0.138` n `421`
- 4h: commodity avg `0.1545` n `12`; crypto_alt avg `-0.1024` n `228`; crypto_major avg `-0.3066` n `8`; equity avg `0.1051` n `69`; fx avg `-0.0414` n `6`; index avg `-0.0216` n `23`; metal avg `-0.0298` n `18`; unknown avg `-0.2466` n `421`
- 24h: commodity avg `0.2995` n `12`; crypto_alt avg `0.3349` n `228`; crypto_major avg `1.3565` n `8`; equity avg `1.0666` n `69`; fx avg `-0.0017` n `6`; index avg `-0.0746` n `23`; metal avg `-0.0959` n `18`; unknown avg `0.6497` n `401`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
