# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T03:22:21.016545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `12`; crypto_alt avg `-0.166` n `228`; crypto_major avg `-0.1121` n `8`; equity avg `0.0203` n `69`; fx avg `0.0013` n `6`; index avg `0.0025` n `23`; metal avg `-0.0123` n `18`; unknown avg `-0.0818` n `419`
- 1h: commodity avg `0.0463` n `12`; crypto_alt avg `0.0871` n `228`; crypto_major avg `-0.0026` n `8`; equity avg `0.0943` n `69`; fx avg `0.0024` n `6`; index avg `-0.0057` n `23`; metal avg `0.0047` n `18`; unknown avg `-0.243` n `419`
- 4h: commodity avg `-0.0819` n `12`; crypto_alt avg `1.6733` n `228`; crypto_major avg `1.3922` n `8`; equity avg `0.3389` n `69`; fx avg `0.0063` n `6`; index avg `-0.0041` n `23`; metal avg `0.0452` n `18`; unknown avg `-0.2079` n `419`
- 24h: commodity avg `-0.0889` n `12`; crypto_alt avg `2.3257` n `228`; crypto_major avg `2.2104` n `8`; equity avg `1.1375` n `69`; fx avg `0.1056` n `6`; index avg `0.1348` n `23`; metal avg `0.1649` n `18`; unknown avg `0.5155` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
