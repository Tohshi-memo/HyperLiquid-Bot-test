# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T17:37:31.005321+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0331` n `13`; crypto_alt avg `0.0396` n `235`; crypto_major avg `0.0428` n `8`; equity avg `0.0654` n `144`; fx avg `0.0108` n `6`; index avg `0.0019` n `26`; metal avg `-0.0297` n `20`; unknown avg `0.9669` n `1079`
- 1h: commodity avg `-0.0568` n `13`; crypto_alt avg `0.0417` n `235`; crypto_major avg `0.1607` n `8`; equity avg `0.0825` n `144`; fx avg `0.0116` n `6`; index avg `0.0195` n `26`; metal avg `-0.0153` n `20`; unknown avg `0.5739` n `1077`
- 4h: commodity avg `0.0302` n `13`; crypto_alt avg `-0.8688` n `235`; crypto_major avg `-0.4956` n `8`; equity avg `0.3305` n `144`; fx avg `0.0041` n `6`; index avg `0.1055` n `26`; metal avg `-0.1145` n `20`; unknown avg `-0.0096` n `989`
- 24h: commodity avg `-0.3353` n `13`; crypto_alt avg `-0.0425` n `235`; crypto_major avg `0.0856` n `8`; equity avg `0.3019` n `144`; fx avg `-0.1023` n `6`; index avg `0.1179` n `26`; metal avg `0.0913` n `20`; unknown avg `-0.1645` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2004`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
