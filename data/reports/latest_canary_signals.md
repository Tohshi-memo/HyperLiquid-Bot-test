# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T04:52:15.243530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0207` n `12`; crypto_alt avg `0.5776` n `228`; crypto_major avg `0.337` n `8`; equity avg `0.0943` n `69`; fx avg `-0.0013` n `6`; index avg `0.019` n `23`; metal avg `0.0323` n `18`; unknown avg `0.1278` n `419`
- 1h: commodity avg `-0.1286` n `12`; crypto_alt avg `-0.4855` n `228`; crypto_major avg `-0.4371` n `8`; equity avg `0.0224` n `69`; fx avg `-0.003` n `6`; index avg `0.0265` n `23`; metal avg `-0.0305` n `18`; unknown avg `-0.2045` n `419`
- 4h: commodity avg `-0.2228` n `12`; crypto_alt avg `0.1677` n `228`; crypto_major avg `0.1925` n `8`; equity avg `0.1543` n `69`; fx avg `-0.0026` n `6`; index avg `-0.0581` n `23`; metal avg `-0.024` n `18`; unknown avg `-0.6663` n `419`
- 24h: commodity avg `-0.2786` n `12`; crypto_alt avg `1.6061` n `228`; crypto_major avg `1.6819` n `8`; equity avg `0.8154` n `69`; fx avg `0.091` n `6`; index avg `0.0679` n `23`; metal avg `-0.0784` n `18`; unknown avg `0.7063` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
