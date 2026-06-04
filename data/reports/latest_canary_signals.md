# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T05:37:23.434518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0512` n `12`; crypto_alt avg `0.4926` n `228`; crypto_major avg `0.5015` n `8`; equity avg `0.1915` n `73`; fx avg `-0.0042` n `6`; index avg `0.0186` n `23`; metal avg `-0.0556` n `18`; unknown avg `-0.1336` n `420`
- 1h: commodity avg `-0.021` n `12`; crypto_alt avg `-1.0463` n `228`; crypto_major avg `-0.8779` n `8`; equity avg `-0.1547` n `73`; fx avg `0.0054` n `6`; index avg `-0.0593` n `23`; metal avg `-0.3047` n `18`; unknown avg `-1.0024` n `420`
- 4h: commodity avg `0.109` n `12`; crypto_alt avg `-1.5857` n `228`; crypto_major avg `0.4917` n `8`; equity avg `0.2614` n `73`; fx avg `-0.0032` n `6`; index avg `-0.0893` n `23`; metal avg `-0.1111` n `18`; unknown avg `0.1108` n `420`
- 24h: commodity avg `0.0457` n `12`; crypto_alt avg `-3.973` n `228`; crypto_major avg `-3.1465` n `8`; equity avg `-3.5827` n `73`; fx avg `-0.0341` n `6`; index avg `-1.0538` n `23`; metal avg `-1.3566` n `18`; unknown avg `-0.2866` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
