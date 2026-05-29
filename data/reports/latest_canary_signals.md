# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T15:52:27.707923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0945` n `12`; crypto_alt avg `-0.5005` n `228`; crypto_major avg `-0.4988` n `8`; equity avg `0.0223` n `69`; fx avg `0.005` n `6`; index avg `0.0562` n `23`; metal avg `-0.0964` n `18`; unknown avg `-0.3693` n `418`
- 1h: commodity avg `-0.1394` n `12`; crypto_alt avg `1.5446` n `228`; crypto_major avg `1.3672` n `8`; equity avg `0.8264` n `69`; fx avg `0.0707` n `6`; index avg `0.1157` n `23`; metal avg `-0.0375` n `18`; unknown avg `1.2395` n `418`
- 4h: commodity avg `-0.2688` n `12`; crypto_alt avg `1.4019` n `228`; crypto_major avg `1.2657` n `8`; equity avg `0.4994` n `69`; fx avg `0.1343` n `6`; index avg `-0.2022` n `23`; metal avg `0.0611` n `18`; unknown avg `0.2511` n `417`
- 24h: commodity avg `-0.6763` n `12`; crypto_alt avg `2.742` n `228`; crypto_major avg `2.6971` n `8`; equity avg `2.0767` n `69`; fx avg `0.2099` n `6`; index avg `0.0869` n `23`; metal avg `0.7425` n `18`; unknown avg `1.339` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
