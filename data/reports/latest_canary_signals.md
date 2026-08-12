# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T00:37:27.711070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `0.0312` n `230`; crypto_major avg `0.0784` n `8`; equity avg `-0.0168` n `113`; fx avg `-0.0079` n `6`; index avg `0.0124` n `25`; metal avg `0.0468` n `20`; unknown avg `0.0442` n `786`
- 1h: commodity avg `0.05` n `12`; crypto_alt avg `0.1161` n `230`; crypto_major avg `0.0043` n `8`; equity avg `0.1909` n `113`; fx avg `0.0112` n `6`; index avg `0.044` n `25`; metal avg `0.0894` n `20`; unknown avg `-0.0937` n `786`
- 4h: commodity avg `0.0522` n `12`; crypto_alt avg `0.1271` n `230`; crypto_major avg `0.2347` n `8`; equity avg `0.3372` n `113`; fx avg `0.013` n `6`; index avg `0.0218` n `25`; metal avg `0.0826` n `20`; unknown avg `-0.0453` n `785`
- 24h: commodity avg `0.1877` n `12`; crypto_alt avg `-1.1809` n `230`; crypto_major avg `0.8874` n `8`; equity avg `1.5084` n `113`; fx avg `-0.0152` n `6`; index avg `0.1609` n `25`; metal avg `-0.2438` n `20`; unknown avg `-0.0705` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2252`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2187`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2033`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1977`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
