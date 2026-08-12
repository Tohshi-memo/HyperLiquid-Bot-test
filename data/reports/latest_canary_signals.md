# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T05:07:32.142494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0249` n `12`; crypto_alt avg `-0.0645` n `230`; crypto_major avg `-0.1065` n `8`; equity avg `-0.0491` n `113`; fx avg `-0.0017` n `6`; index avg `-0.0107` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.151` n `786`
- 1h: commodity avg `-0.0679` n `12`; crypto_alt avg `-0.1598` n `230`; crypto_major avg `-0.1133` n `8`; equity avg `-0.0971` n `113`; fx avg `-0.0028` n `6`; index avg `-0.0331` n `25`; metal avg `0.0234` n `20`; unknown avg `-0.1256` n `786`
- 4h: commodity avg `0.0141` n `12`; crypto_alt avg `-0.0416` n `230`; crypto_major avg `-0.245` n `8`; equity avg `0.6278` n `113`; fx avg `0.0402` n `6`; index avg `0.1105` n `25`; metal avg `0.1047` n `20`; unknown avg `-0.3442` n `786`
- 24h: commodity avg `0.2259` n `12`; crypto_alt avg `-1.1117` n `230`; crypto_major avg `0.542` n `8`; equity avg `1.5942` n `113`; fx avg `0.0243` n `6`; index avg `0.0911` n `25`; metal avg `-0.0412` n `20`; unknown avg `-0.1241` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2218`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2186`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2108`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1978`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
