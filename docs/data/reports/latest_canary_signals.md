# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T06:22:31.371795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0292` n `12`; crypto_alt avg `0.034` n `230`; crypto_major avg `0.0275` n `8`; equity avg `0.0133` n `107`; fx avg `-0.0058` n `6`; index avg `0.0216` n `25`; metal avg `-0.0129` n `20`; unknown avg `0.0002` n `781`
- 1h: commodity avg `-0.0436` n `12`; crypto_alt avg `0.1159` n `230`; crypto_major avg `-0.021` n `8`; equity avg `0.6889` n `107`; fx avg `0.0315` n `6`; index avg `0.1512` n `25`; metal avg `0.0457` n `20`; unknown avg `0.0149` n `765`
- 4h: commodity avg `0.029` n `12`; crypto_alt avg `0.0699` n `230`; crypto_major avg `0.0888` n `8`; equity avg `0.8632` n `107`; fx avg `0.0855` n `6`; index avg `0.1439` n `25`; metal avg `0.1412` n `20`; unknown avg `-0.0185` n `764`
- 24h: commodity avg `0.3506` n `12`; crypto_alt avg `1.2084` n `230`; crypto_major avg `1.2211` n `8`; equity avg `2.3994` n `107`; fx avg `0.07` n `6`; index avg `0.2617` n `25`; metal avg `-0.0514` n `20`; unknown avg `0.1671` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
