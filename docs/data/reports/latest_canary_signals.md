# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T09:37:27.606515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0456` n `12`; crypto_alt avg `-0.0626` n `230`; crypto_major avg `-0.0241` n `8`; equity avg `0.0246` n `113`; fx avg `0.0045` n `6`; index avg `0.0183` n `25`; metal avg `0.026` n `20`; unknown avg `-0.0153` n `785`
- 1h: commodity avg `-0.0364` n `12`; crypto_alt avg `0.053` n `230`; crypto_major avg `0.1995` n `8`; equity avg `0.1424` n `113`; fx avg `-0.0051` n `6`; index avg `0.0456` n `25`; metal avg `0.0544` n `20`; unknown avg `0.0471` n `785`
- 4h: commodity avg `0.3438` n `12`; crypto_alt avg `-0.287` n `230`; crypto_major avg `0.0869` n `8`; equity avg `-0.3337` n `113`; fx avg `0.0205` n `6`; index avg `-0.0286` n `25`; metal avg `0.1496` n `20`; unknown avg `0.0593` n `753`
- 24h: commodity avg `1.0234` n `12`; crypto_alt avg `-1.1062` n `230`; crypto_major avg `-0.6017` n `8`; equity avg `-1.5535` n `113`; fx avg `0.0207` n `6`; index avg `-0.015` n `25`; metal avg `0.3241` n `20`; unknown avg `0.1769` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
