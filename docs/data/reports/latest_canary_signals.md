# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T09:37:27.240314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.025` n `12`; crypto_alt avg `-0.1259` n `230`; crypto_major avg `-0.1893` n `8`; equity avg `-0.1629` n `98`; fx avg `0.0198` n `6`; index avg `-0.0258` n `25`; metal avg `0.0141` n `20`; unknown avg `-0.0084` n `773`
- 1h: commodity avg `0.108` n `12`; crypto_alt avg `0.0569` n `230`; crypto_major avg `-0.0665` n `8`; equity avg `0.0385` n `98`; fx avg `0.0017` n `6`; index avg `0.003` n `25`; metal avg `0.024` n `20`; unknown avg `-0.0218` n `773`
- 4h: commodity avg `0.3745` n `12`; crypto_alt avg `-0.0217` n `230`; crypto_major avg `-0.2152` n `8`; equity avg `-0.1818` n `98`; fx avg `-0.036` n `6`; index avg `-0.0929` n `25`; metal avg `-0.1008` n `20`; unknown avg `-0.0277` n `739`
- 24h: commodity avg `0.7156` n `12`; crypto_alt avg `-0.8031` n `230`; crypto_major avg `-1.7162` n `8`; equity avg `0.3627` n `98`; fx avg `-0.0038` n `6`; index avg `-0.0179` n `25`; metal avg `0.3317` n `20`; unknown avg `0.0782` n `739`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1063`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0785`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0706`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.068`, n `666`, weak_sample_signal
