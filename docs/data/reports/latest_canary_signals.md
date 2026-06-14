# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T09:52:30.721603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `0.0857` n `228`; crypto_major avg `0.2046` n `8`; equity avg `0.071` n `74`; fx avg `0.0056` n `6`; index avg `-0.0411` n `23`; metal avg `-0.004` n `18`; unknown avg `0.0212` n `645`
- 1h: commodity avg `0.1442` n `12`; crypto_alt avg `0.0948` n `228`; crypto_major avg `0.1571` n `8`; equity avg `0.1375` n `74`; fx avg `-0.0141` n `6`; index avg `-0.0412` n `23`; metal avg `-0.0029` n `18`; unknown avg `-0.2321` n `629`
- 4h: commodity avg `-0.1438` n `12`; crypto_alt avg `0.1593` n `228`; crypto_major avg `0.1016` n `8`; equity avg `0.2992` n `74`; fx avg `-0.0227` n `6`; index avg `-0.019` n `23`; metal avg `0.0128` n `18`; unknown avg `1.9567` n `609`
- 24h: commodity avg `-0.6659` n `12`; crypto_alt avg `0.4468` n `228`; crypto_major avg `1.136` n `8`; equity avg `0.9015` n `74`; fx avg `-0.0304` n `6`; index avg `0.2103` n `23`; metal avg `0.1837` n `18`; unknown avg `-1.2005` n `591`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
