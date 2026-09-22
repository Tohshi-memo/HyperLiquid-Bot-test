# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T13:52:29.182905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.093` n `12`; crypto_alt avg `0.2984` n `234`; crypto_major avg `0.4151` n `8`; equity avg `0.3932` n `140`; fx avg `-0.0455` n `6`; index avg `0.0539` n `26`; metal avg `0.0343` n `20`; unknown avg `3.8413` n `920`
- 1h: commodity avg `0.1176` n `12`; crypto_alt avg `0.2223` n `234`; crypto_major avg `0.4344` n `8`; equity avg `1.0058` n `140`; fx avg `-0.0414` n `6`; index avg `0.1338` n `26`; metal avg `0.0647` n `20`; unknown avg `35.9576` n `918`
- 4h: commodity avg `0.2067` n `12`; crypto_alt avg `0.4356` n `234`; crypto_major avg `0.5313` n `8`; equity avg `0.8496` n `140`; fx avg `0.01` n `6`; index avg `0.1087` n `26`; metal avg `0.1994` n `20`; unknown avg `2.8989` n `910`
- 24h: commodity avg `-0.3107` n `12`; crypto_alt avg `0.8744` n `234`; crypto_major avg `1.512` n `8`; equity avg `1.5822` n `140`; fx avg `-0.2797` n `6`; index avg `0.3189` n `26`; metal avg `-0.0274` n `20`; unknown avg `3.2249` n `788`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
