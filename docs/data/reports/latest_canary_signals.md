# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T18:37:13.871869+00:00`
- Correlation status: `ready`
- Asset price records: `670`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0716` n `12`; crypto_alt avg `0.1683` n `228`; crypto_major avg `0.1163` n `8`; equity avg `0.09` n `65`; fx avg `0.0038` n `5`; index avg `-0.0998` n `23`; metal avg `-0.084` n `18`; unknown avg `0.2805` n `375`
- 1h: commodity avg `-0.275` n `12`; crypto_alt avg `0.5702` n `228`; crypto_major avg `0.5198` n `8`; equity avg `0.276` n `65`; fx avg `0.0103` n `5`; index avg `-0.0271` n `23`; metal avg `0.135` n `18`; unknown avg `0.0443` n `375`
- 4h: commodity avg `-0.3008` n `12`; crypto_alt avg `1.9207` n `228`; crypto_major avg `1.41` n `8`; equity avg `1.032` n `65`; fx avg `-0.0054` n `5`; index avg `0.4753` n `23`; metal avg `0.1758` n `18`; unknown avg `0.3193` n `375`
- 24h: commodity avg `0.0825` n `12`; crypto_alt avg `2.9986` n `228`; crypto_major avg `1.2013` n `8`; equity avg `3.0753` n `65`; fx avg `0.175` n `5`; index avg `1.5286` n `23`; metal avg `0.6951` n `18`; unknown avg `0.5989` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1221`, n `662`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1179`, n `662`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1089`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `662`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0935`, n `662`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0691`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `662`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0588`, n `662`, weak_sample_signal
