# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T19:16:29.275280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1016` n `12`; crypto_alt avg `-0.1494` n `228`; crypto_major avg `-0.1678` n `8`; equity avg `-0.1373` n `69`; fx avg `-0.0027` n `6`; index avg `-0.1043` n `23`; metal avg `-0.0558` n `18`; unknown avg `-0.0166` n `417`
- 1h: commodity avg `0.1877` n `12`; crypto_alt avg `-0.4982` n `228`; crypto_major avg `-0.3524` n `8`; equity avg `-0.2883` n `69`; fx avg `-0.0032` n `6`; index avg `-0.1456` n `23`; metal avg `-0.1866` n `18`; unknown avg `0.1351` n `417`
- 4h: commodity avg `-0.1172` n `12`; crypto_alt avg `2.1173` n `228`; crypto_major avg `1.8454` n `8`; equity avg `0.65` n `69`; fx avg `-0.0088` n `6`; index avg `0.203` n `23`; metal avg `0.6481` n `18`; unknown avg `0.4397` n `417`
- 24h: commodity avg `1.0413` n `12`; crypto_alt avg `-3.6338` n `228`; crypto_major avg `-1.129` n `8`; equity avg `1.5548` n `69`; fx avg `-0.0236` n `6`; index avg `0.8513` n `23`; metal avg `0.5343` n `18`; unknown avg `-0.7` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1903`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
