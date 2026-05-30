# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T04:14:26.393606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0674` n `12`; crypto_alt avg `-0.0726` n `228`; crypto_major avg `-0.0564` n `8`; equity avg `-0.0124` n `69`; fx avg `-0.0006` n `6`; index avg `-0.0012` n `23`; metal avg `-0.0503` n `18`; unknown avg `0.6194` n `419`
- 1h: commodity avg `0.0827` n `12`; crypto_alt avg `-0.5297` n `228`; crypto_major avg `-0.3258` n `8`; equity avg `-0.0613` n `69`; fx avg `0.0014` n `6`; index avg `0.0084` n `23`; metal avg `-0.0683` n `18`; unknown avg `0.536` n `419`
- 4h: commodity avg `-0.0826` n `12`; crypto_alt avg `1.0429` n `228`; crypto_major avg `0.9234` n `8`; equity avg `0.3231` n `69`; fx avg `0.0017` n `6`; index avg `-0.0705` n `23`; metal avg `-0.0408` n `18`; unknown avg `-0.6811` n `419`
- 24h: commodity avg `-0.1812` n `12`; crypto_alt avg `2.3656` n `228`; crypto_major avg `2.2506` n `8`; equity avg `1.0332` n `69`; fx avg `0.1067` n `6`; index avg `0.1071` n `23`; metal avg `0.0781` n `18`; unknown avg `1.6603` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
