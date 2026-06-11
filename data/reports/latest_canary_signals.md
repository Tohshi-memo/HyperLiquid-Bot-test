# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T16:59:46.904956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1578` n `12`; crypto_alt avg `-0.5565` n `228`; crypto_major avg `-0.3663` n `8`; equity avg `-0.6499` n `74`; fx avg `0.0017` n `6`; index avg `-0.2421` n `23`; metal avg `-0.2376` n `18`; unknown avg `-0.4435` n `556`
- 1h: commodity avg `-0.0864` n `12`; crypto_alt avg `-0.2089` n `228`; crypto_major avg `-0.1354` n `8`; equity avg `-0.2836` n `74`; fx avg `-0.0141` n `6`; index avg `-0.1159` n `23`; metal avg `-0.3515` n `18`; unknown avg `-0.6626` n `556`
- 4h: commodity avg `-0.1457` n `12`; crypto_alt avg `-0.0411` n `228`; crypto_major avg `-0.287` n `8`; equity avg `-0.0549` n `74`; fx avg `-0.1058` n `6`; index avg `0.042` n `23`; metal avg `0.2294` n `18`; unknown avg `-0.3419` n `556`
- 24h: commodity avg `-0.669` n `12`; crypto_alt avg `0.7551` n `228`; crypto_major avg `0.5481` n `8`; equity avg `-0.2307` n `74`; fx avg `-0.0713` n `6`; index avg `0.0651` n `23`; metal avg `-0.7536` n `18`; unknown avg `1.7529` n `528`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
