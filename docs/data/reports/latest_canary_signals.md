# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T15:16:17.007442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `0.0513` n `230`; crypto_major avg `0.0628` n `8`; equity avg `0.0502` n `102`; fx avg `0.0037` n `6`; index avg `-0.0081` n `25`; metal avg `-0.0038` n `20`; unknown avg `-0.0071` n `782`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `0.1339` n `230`; crypto_major avg `0.138` n `8`; equity avg `0.0732` n `102`; fx avg `0.0218` n `6`; index avg `0.0252` n `25`; metal avg `0.0096` n `20`; unknown avg `1.7488` n `782`
- 4h: commodity avg `-0.0903` n `12`; crypto_alt avg `0.0713` n `230`; crypto_major avg `0.1013` n `8`; equity avg `-0.0745` n `102`; fx avg `-0.0543` n `6`; index avg `-0.018` n `25`; metal avg `0.0071` n `20`; unknown avg `1.1073` n `782`
- 24h: commodity avg `-1.0971` n `12`; crypto_alt avg `0.3475` n `230`; crypto_major avg `0.1841` n `8`; equity avg `0.9139` n `102`; fx avg `-0.1535` n `6`; index avg `0.222` n `25`; metal avg `0.2264` n `20`; unknown avg `1.4291` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
