# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T11:07:34.888203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0647` n `12`; crypto_alt avg `-0.0596` n `230`; crypto_major avg `-0.0162` n `8`; equity avg `-0.1981` n `99`; fx avg `-0.0052` n `6`; index avg `-0.0352` n `25`; metal avg `-0.0561` n `20`; unknown avg `-0.0184` n `772`
- 1h: commodity avg `0.1237` n `12`; crypto_alt avg `-0.0741` n `230`; crypto_major avg `0.0399` n `8`; equity avg `-0.0412` n `99`; fx avg `-0.009` n `6`; index avg `0.006` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.0172` n `772`
- 4h: commodity avg `0.1865` n `12`; crypto_alt avg `-0.0678` n `230`; crypto_major avg `0.1079` n `8`; equity avg `0.2405` n `99`; fx avg `-0.0232` n `6`; index avg `0.0236` n `25`; metal avg `-0.2046` n `20`; unknown avg `0.0214` n `772`
- 24h: commodity avg `0.7866` n `12`; crypto_alt avg `-0.4472` n `230`; crypto_major avg `-0.2172` n `8`; equity avg `0.4356` n `99`; fx avg `-0.0893` n `6`; index avg `0.1438` n `25`; metal avg `-0.3717` n `20`; unknown avg `11.3869` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0783`, n `666`, weak_sample_signal
