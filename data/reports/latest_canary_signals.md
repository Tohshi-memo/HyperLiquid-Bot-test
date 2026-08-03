# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T08:09:34.559845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1235` n `12`; crypto_alt avg `0.0304` n `230`; crypto_major avg `0.0057` n `8`; equity avg `-0.1617` n `102`; fx avg `-0.0104` n `6`; index avg `-0.0491` n `25`; metal avg `-0.0381` n `20`; unknown avg `-0.0167` n `784`
- 1h: commodity avg `0.137` n `12`; crypto_alt avg `-0.0174` n `230`; crypto_major avg `-0.0672` n `8`; equity avg `-0.3564` n `102`; fx avg `-0.0288` n `6`; index avg `-0.0504` n `25`; metal avg `0.0455` n `20`; unknown avg `-0.0401` n `784`
- 4h: commodity avg `0.0819` n `12`; crypto_alt avg `-0.255` n `230`; crypto_major avg `-0.4179` n `8`; equity avg `-0.6134` n `102`; fx avg `0.0057` n `6`; index avg `-0.0601` n `25`; metal avg `-0.0316` n `20`; unknown avg `-0.0137` n `768`
- 24h: commodity avg `-0.0706` n `12`; crypto_alt avg `-1.1892` n `230`; crypto_major avg `-0.8317` n `8`; equity avg `0.1079` n `102`; fx avg `-0.2011` n `6`; index avg `-0.0929` n `25`; metal avg `-0.0863` n `20`; unknown avg `0.9774` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
