# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T08:37:30.394120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0798` n `12`; crypto_alt avg `0.004` n `230`; crypto_major avg `-0.0284` n `8`; equity avg `0.0307` n `113`; fx avg `0.0285` n `6`; index avg `-0.0076` n `25`; metal avg `0.0302` n `20`; unknown avg `0.5025` n `787`
- 1h: commodity avg `-0.1421` n `12`; crypto_alt avg `-0.1643` n `230`; crypto_major avg `-0.2267` n `8`; equity avg `-0.2301` n `113`; fx avg `0.0318` n `6`; index avg `-0.0367` n `25`; metal avg `-0.0611` n `20`; unknown avg `0.4457` n `787`
- 4h: commodity avg `-0.2233` n `12`; crypto_alt avg `0.0374` n `230`; crypto_major avg `0.1684` n `8`; equity avg `-0.6526` n `113`; fx avg `0.0951` n `6`; index avg `-0.0739` n `25`; metal avg `-0.2603` n `20`; unknown avg `-0.0185` n `755`
- 24h: commodity avg `-0.3652` n `12`; crypto_alt avg `-0.4417` n `230`; crypto_major avg `0.2637` n `8`; equity avg `1.3334` n `113`; fx avg `0.0408` n `6`; index avg `0.1702` n `25`; metal avg `-0.5263` n `20`; unknown avg `0.1187` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2477`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
