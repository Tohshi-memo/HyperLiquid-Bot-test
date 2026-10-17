# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T04:17:11.008205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `13`; crypto_alt avg `0.017` n `236`; crypto_major avg `-0.0266` n `8`; equity avg `-0.047` n `151`; fx avg `-0.0011` n `6`; index avg `-0.0102` n `26`; metal avg `-0.0003` n `20`; unknown avg `-0.0778` n `1193`
- 1h: commodity avg `0.0058` n `13`; crypto_alt avg `0.2232` n `236`; crypto_major avg `0.0395` n `8`; equity avg `0.0065` n `151`; fx avg `-0.0031` n `6`; index avg `0.0047` n `26`; metal avg `0.0141` n `20`; unknown avg `-0.2042` n `1185`
- 4h: commodity avg `-0.0546` n `13`; crypto_alt avg `0.0268` n `236`; crypto_major avg `-0.0143` n `8`; equity avg `0.1813` n `151`; fx avg `-0.0079` n `6`; index avg `0.0216` n `26`; metal avg `0.0152` n `20`; unknown avg `0.6636` n `1183`
- 24h: commodity avg `0.6219` n `13`; crypto_alt avg `-1.3233` n `236`; crypto_major avg `-1.0922` n `8`; equity avg `-4.2688` n `151`; fx avg `-0.0637` n `6`; index avg `-0.6874` n `26`; metal avg `-0.2803` n `20`; unknown avg `40.5516` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1731`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0928`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0764`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
