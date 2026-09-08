# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T17:37:30.593677+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0143` n `12`; crypto_alt avg `0.0431` n `233`; crypto_major avg `0.1251` n `8`; equity avg `0.0158` n `134`; fx avg `0.0071` n `6`; index avg `0.0084` n `26`; metal avg `-0.0048` n `20`; unknown avg `-0.3489` n `797`
- 1h: commodity avg `-0.0185` n `12`; crypto_alt avg `-0.3585` n `233`; crypto_major avg `-0.2045` n `8`; equity avg `0.1799` n `134`; fx avg `0.009` n `6`; index avg `0.0381` n `26`; metal avg `0.045` n `20`; unknown avg `0.1596` n `771`
- 4h: commodity avg `-0.3801` n `12`; crypto_alt avg `1.4286` n `232`; crypto_major avg `1.4983` n `8`; equity avg `0.8869` n `134`; fx avg `0.0456` n `6`; index avg `0.0227` n `26`; metal avg `0.0157` n `20`; unknown avg `-0.2205` n `759`
- 24h: commodity avg `-0.3361` n `12`; crypto_alt avg `0.6161` n `232`; crypto_major avg `0.3566` n `8`; equity avg `1.0455` n `134`; fx avg `-0.0533` n `6`; index avg `-0.0393` n `26`; metal avg `-0.0235` n `20`; unknown avg `7062.1528` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
