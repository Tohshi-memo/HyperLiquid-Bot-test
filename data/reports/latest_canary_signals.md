# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T14:52:29.415175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `-0.3781` n `230`; crypto_major avg `-0.2322` n `8`; equity avg `0.2585` n `113`; fx avg `-0.0061` n `6`; index avg `0.0367` n `25`; metal avg `0.0079` n `20`; unknown avg `-0.0161` n `785`
- 1h: commodity avg `0.0849` n `12`; crypto_alt avg `-0.5159` n `230`; crypto_major avg `-0.5022` n `8`; equity avg `0.7272` n `113`; fx avg `0.026` n `6`; index avg `0.0907` n `25`; metal avg `0.0431` n `20`; unknown avg `0.0311` n `785`
- 4h: commodity avg `-0.1406` n `12`; crypto_alt avg `-0.6982` n `230`; crypto_major avg `-0.5431` n `8`; equity avg `0.733` n `113`; fx avg `-0.0169` n `6`; index avg `0.0686` n `25`; metal avg `-0.0699` n `20`; unknown avg `-0.143` n `785`
- 24h: commodity avg `0.1796` n `12`; crypto_alt avg `-1.6276` n `230`; crypto_major avg `-0.6357` n `8`; equity avg `0.3866` n `113`; fx avg `-0.0658` n `6`; index avg `0.1434` n `25`; metal avg `0.2441` n `20`; unknown avg `-0.2441` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2008`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1949`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1874`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
