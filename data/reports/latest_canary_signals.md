# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T13:22:36.143345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0376` n `12`; crypto_alt avg `-0.1105` n `230`; crypto_major avg `-0.0999` n `8`; equity avg `-0.0545` n `113`; fx avg `0.0084` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0479` n `20`; unknown avg `-0.0482` n `787`
- 1h: commodity avg `-0.2138` n `12`; crypto_alt avg `0.0044` n `230`; crypto_major avg `0.1807` n `8`; equity avg `0.1786` n `113`; fx avg `0.0066` n `6`; index avg `0.0431` n `25`; metal avg `-0.0367` n `20`; unknown avg `0.1279` n `787`
- 4h: commodity avg `-0.1561` n `12`; crypto_alt avg `-0.0137` n `230`; crypto_major avg `0.0138` n `8`; equity avg `0.3318` n `113`; fx avg `-0.0031` n `6`; index avg `0.0896` n `25`; metal avg `0.0913` n `20`; unknown avg `0.0199` n `787`
- 24h: commodity avg `-0.4445` n `12`; crypto_alt avg `-0.7947` n `230`; crypto_major avg `-0.3645` n `8`; equity avg `0.3932` n `113`; fx avg `0.0357` n `6`; index avg `0.0358` n `25`; metal avg `-0.5002` n `20`; unknown avg `0.3203` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2301`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1983`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
