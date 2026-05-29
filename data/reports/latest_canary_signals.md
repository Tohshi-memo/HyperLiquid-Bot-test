# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T11:07:21.183132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1008` n `12`; crypto_alt avg `0.0118` n `228`; crypto_major avg `-0.007` n `8`; equity avg `-0.0495` n `69`; fx avg `-0.0043` n `6`; index avg `0.0474` n `23`; metal avg `-0.0642` n `18`; unknown avg `0.0215` n `417`
- 1h: commodity avg `0.0546` n `12`; crypto_alt avg `-0.3479` n `228`; crypto_major avg `-0.1556` n `8`; equity avg `-0.0181` n `69`; fx avg `-0.001` n `6`; index avg `0.1544` n `23`; metal avg `0.0833` n `18`; unknown avg `-0.0157` n `417`
- 4h: commodity avg `0.0972` n `12`; crypto_alt avg `-0.258` n `228`; crypto_major avg `-0.0201` n `8`; equity avg `-0.3372` n `69`; fx avg `-0.0467` n `6`; index avg `0.0782` n `23`; metal avg `-0.0063` n `18`; unknown avg `-0.0257` n `417`
- 24h: commodity avg `0.0814` n `12`; crypto_alt avg `1.906` n `228`; crypto_major avg `2.2375` n `8`; equity avg `3.7266` n `69`; fx avg `0.1739` n `6`; index avg `1.5758` n `23`; metal avg `2.1869` n `18`; unknown avg `0.7145` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
