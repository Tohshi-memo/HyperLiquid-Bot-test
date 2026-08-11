# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T07:07:28.327803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0494` n `12`; crypto_alt avg `-0.0038` n `230`; crypto_major avg `0.0772` n `8`; equity avg `0.0156` n `113`; fx avg `-0.0036` n `6`; index avg `-0.0064` n `25`; metal avg `-0.0027` n `20`; unknown avg `0.0014` n `785`
- 1h: commodity avg `0.1765` n `12`; crypto_alt avg `-0.1919` n `230`; crypto_major avg `-0.1471` n `8`; equity avg `-0.2375` n `113`; fx avg `0.0144` n `6`; index avg `-0.0509` n `25`; metal avg `-0.1195` n `20`; unknown avg `0.0206` n `785`
- 4h: commodity avg `0.2108` n `12`; crypto_alt avg `-0.4227` n `230`; crypto_major avg `-0.2766` n `8`; equity avg `-0.2957` n `113`; fx avg `0.0244` n `6`; index avg `-0.0538` n `25`; metal avg `-0.3159` n `20`; unknown avg `-0.0424` n `753`
- 24h: commodity avg `1.0382` n `12`; crypto_alt avg `-1.1829` n `230`; crypto_major avg `-1.1246` n `8`; equity avg `-1.4473` n `113`; fx avg `0.0491` n `6`; index avg `-0.0475` n `25`; metal avg `0.013` n `20`; unknown avg `0.1189` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
