# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T00:52:22.874387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `-0.1737` n `228`; crypto_major avg `-0.2792` n `8`; equity avg `-0.0222` n `74`; fx avg `0.0016` n `6`; index avg `-0.0136` n `23`; metal avg `0.002` n `18`; unknown avg `-0.0102` n `516`
- 1h: commodity avg `-0.0241` n `12`; crypto_alt avg `0.3577` n `228`; crypto_major avg `0.1616` n `8`; equity avg `-0.022` n `74`; fx avg `-0.0036` n `6`; index avg `-0.0298` n `23`; metal avg `0.0355` n `18`; unknown avg `-0.0925` n `515`
- 4h: commodity avg `0.0682` n `12`; crypto_alt avg `1.1513` n `228`; crypto_major avg `0.6041` n `8`; equity avg `0.2642` n `74`; fx avg `-0.0424` n `6`; index avg `-0.067` n `23`; metal avg `0.0902` n `18`; unknown avg `0.0118` n `515`
- 24h: commodity avg `0.1526` n `12`; crypto_alt avg `-1.571` n `228`; crypto_major avg `-1.8319` n `8`; equity avg `-0.4393` n `74`; fx avg `0.0102` n `6`; index avg `-0.0887` n `23`; metal avg `-0.3675` n `18`; unknown avg `0.4337` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
