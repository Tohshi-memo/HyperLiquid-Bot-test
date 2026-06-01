# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T11:37:20.881156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0554` n `12`; crypto_alt avg `-0.0759` n `228`; crypto_major avg `-0.088` n `8`; equity avg `0.0897` n `69`; fx avg `-0.0019` n `6`; index avg `0.037` n `23`; metal avg `0.0424` n `18`; unknown avg `0.9597` n `418`
- 1h: commodity avg `-0.2651` n `12`; crypto_alt avg `0.4217` n `228`; crypto_major avg `0.2635` n `8`; equity avg `-0.2112` n `69`; fx avg `-0.0121` n `6`; index avg `-0.0571` n `23`; metal avg `-0.0098` n `18`; unknown avg `1.0433` n `416`
- 4h: commodity avg `-0.401` n `12`; crypto_alt avg `-0.0518` n `228`; crypto_major avg `0.3674` n `8`; equity avg `-0.2282` n `69`; fx avg `-0.0011` n `6`; index avg `-0.5633` n `23`; metal avg `0.1909` n `18`; unknown avg `1.3174` n `416`
- 24h: commodity avg `0.7163` n `12`; crypto_alt avg `-0.4148` n `228`; crypto_major avg `-0.4169` n `8`; equity avg `-0.2696` n `69`; fx avg `0.0025` n `6`; index avg `0.5442` n `23`; metal avg `0.3577` n `18`; unknown avg `3.3457` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2873`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2122`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
