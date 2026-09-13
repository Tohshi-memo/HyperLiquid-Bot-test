# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T05:22:36.088997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `0.1317` n `233`; crypto_major avg `0.0658` n `8`; equity avg `-0.0182` n `136`; fx avg `0.0039` n `6`; index avg `-0.0049` n `26`; metal avg `0.0005` n `20`; unknown avg `49.3135` n `838`
- 1h: commodity avg `0.0188` n `12`; crypto_alt avg `0.172` n `233`; crypto_major avg `0.112` n `8`; equity avg `-0.0523` n `136`; fx avg `-0.0039` n `6`; index avg `-0.017` n `26`; metal avg `0.0026` n `20`; unknown avg `50.771` n `830`
- 4h: commodity avg `0.0519` n `12`; crypto_alt avg `0.1649` n `233`; crypto_major avg `-0.1405` n `8`; equity avg `-0.2277` n `136`; fx avg `0.0046` n `6`; index avg `-0.0468` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.0193` n `806`
- 24h: commodity avg `0.1114` n `12`; crypto_alt avg `1.3132` n `233`; crypto_major avg `0.2291` n `8`; equity avg `-0.5538` n `136`; fx avg `-0.0079` n `6`; index avg `-0.0737` n `26`; metal avg `0.0335` n `20`; unknown avg `0.2138` n `710`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
