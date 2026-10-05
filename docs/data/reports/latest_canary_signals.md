# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T08:07:31.466802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `13`; crypto_alt avg `0.0565` n `235`; crypto_major avg `0.1341` n `8`; equity avg `0.0505` n `144`; fx avg `-0.0169` n `6`; index avg `0.0041` n `26`; metal avg `0.0372` n `20`; unknown avg `-0.257` n `1005`
- 1h: commodity avg `-0.0345` n `13`; crypto_alt avg `0.2454` n `235`; crypto_major avg `0.2511` n `8`; equity avg `0.0771` n `144`; fx avg `-0.0013` n `6`; index avg `0.0027` n `26`; metal avg `0.1048` n `20`; unknown avg `-0.3508` n `1005`
- 4h: commodity avg `0.047` n `13`; crypto_alt avg `1.1428` n `235`; crypto_major avg `0.9081` n `8`; equity avg `0.113` n `144`; fx avg `0.0198` n `6`; index avg `0.0217` n `26`; metal avg `0.2343` n `20`; unknown avg `-0.2371` n `979`
- 24h: commodity avg `-0.2858` n `13`; crypto_alt avg `1.154` n `235`; crypto_major avg `1.5555` n `8`; equity avg `0.4152` n `144`; fx avg `-0.083` n `6`; index avg `-0.0108` n `26`; metal avg `0.3082` n `20`; unknown avg `-0.1159` n `880`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2018`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
