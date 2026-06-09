# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T13:37:26.559780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2851` n `12`; crypto_alt avg `-0.243` n `228`; crypto_major avg `-0.2315` n `8`; equity avg `-0.2845` n `74`; fx avg `-0.017` n `6`; index avg `-0.1036` n `23`; metal avg `-0.0058` n `18`; unknown avg `-0.0553` n `547`
- 1h: commodity avg `-0.5694` n `12`; crypto_alt avg `-0.5006` n `228`; crypto_major avg `-0.7467` n `8`; equity avg `-0.4592` n `74`; fx avg `-0.0378` n `6`; index avg `-0.2345` n `23`; metal avg `-0.1729` n `18`; unknown avg `-0.3191` n `547`
- 4h: commodity avg `-0.2553` n `12`; crypto_alt avg `0.2806` n `228`; crypto_major avg `-0.6166` n `8`; equity avg `-0.3172` n `74`; fx avg `0.1041` n `6`; index avg `-0.1268` n `23`; metal avg `0.3234` n `18`; unknown avg `0.1725` n `547`
- 24h: commodity avg `-0.6236` n `12`; crypto_alt avg `-1.5077` n `228`; crypto_major avg `-1.601` n `8`; equity avg `1.3303` n `74`; fx avg `0.112` n `6`; index avg `0.3892` n `23`; metal avg `0.1555` n `18`; unknown avg `-1.1401` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
