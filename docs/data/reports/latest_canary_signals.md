# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T04:37:29.048698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.0844` n `230`; crypto_major avg `-0.0652` n `8`; equity avg `0.0003` n `113`; fx avg `0.0148` n `6`; index avg `-0.0006` n `25`; metal avg `-0.0257` n `20`; unknown avg `0.0605` n `787`
- 1h: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.0107` n `230`; crypto_major avg `0.0177` n `8`; equity avg `-0.0523` n `113`; fx avg `0.0381` n `6`; index avg `-0.0089` n `25`; metal avg `-0.0471` n `20`; unknown avg `-0.1427` n `787`
- 4h: commodity avg `0.0416` n `12`; crypto_alt avg `-0.3061` n `230`; crypto_major avg `-0.1738` n `8`; equity avg `-0.3926` n `113`; fx avg `-0.0147` n `6`; index avg `-0.0826` n `25`; metal avg `-0.0814` n `20`; unknown avg `-0.3415` n `787`
- 24h: commodity avg `-0.3819` n `12`; crypto_alt avg `-0.2857` n `230`; crypto_major avg `-0.1963` n `8`; equity avg `0.8216` n `113`; fx avg `0.0229` n `6`; index avg `0.2149` n `25`; metal avg `-0.512` n `20`; unknown avg `0.9562` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2426`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1884`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
