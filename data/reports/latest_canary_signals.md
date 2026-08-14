# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T03:52:28.872657+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.1218` n `230`; crypto_major avg `-0.1273` n `8`; equity avg `-0.0436` n `113`; fx avg `0.0132` n `6`; index avg `-0.0045` n `25`; metal avg `-0.038` n `20`; unknown avg `-0.2415` n `787`
- 1h: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.3691` n `230`; crypto_major avg `-0.3797` n `8`; equity avg `-0.0207` n `113`; fx avg `0.0072` n `6`; index avg `-0.0038` n `25`; metal avg `0.0081` n `20`; unknown avg `-0.2666` n `787`
- 4h: commodity avg `0.0144` n `12`; crypto_alt avg `-0.3693` n `230`; crypto_major avg `-0.308` n `8`; equity avg `-0.3794` n `113`; fx avg `-0.0441` n `6`; index avg `-0.0805` n `25`; metal avg `-0.1866` n `20`; unknown avg `0.2888` n `787`
- 24h: commodity avg `-0.3311` n `12`; crypto_alt avg `-0.4072` n `230`; crypto_major avg `-0.2541` n `8`; equity avg `0.7609` n `113`; fx avg `-0.0082` n `6`; index avg `0.1973` n `25`; metal avg `-0.5683` n `20`; unknown avg `0.9777` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2399`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1861`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
