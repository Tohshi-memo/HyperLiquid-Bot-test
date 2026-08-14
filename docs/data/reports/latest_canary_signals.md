# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T04:07:30.373344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0194` n `12`; crypto_alt avg `0.0958` n `230`; crypto_major avg `0.1399` n `8`; equity avg `-0.0577` n `113`; fx avg `0.0032` n `6`; index avg `-0.0134` n `25`; metal avg `-0.0129` n `20`; unknown avg `0.1864` n `787`
- 1h: commodity avg `0.0316` n `12`; crypto_alt avg `-0.1292` n `230`; crypto_major avg `-0.0302` n `8`; equity avg `0.0175` n `113`; fx avg `0.0128` n `6`; index avg `0.0024` n `25`; metal avg `-0.0062` n `20`; unknown avg `-0.2074` n `787`
- 4h: commodity avg `0.0245` n `12`; crypto_alt avg `-0.3436` n `230`; crypto_major avg `-0.2485` n `8`; equity avg `-0.4537` n `113`; fx avg `-0.0417` n `6`; index avg `-0.1062` n `25`; metal avg `-0.1699` n `20`; unknown avg `0.3956` n `787`
- 24h: commodity avg `-0.3519` n `12`; crypto_alt avg `-0.2657` n `230`; crypto_major avg `-0.1134` n `8`; equity avg `0.6676` n `113`; fx avg `-0.007` n `6`; index avg `0.1643` n `25`; metal avg `-0.5148` n `20`; unknown avg `0.9912` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2403`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1873`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
