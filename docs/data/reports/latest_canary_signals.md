# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T20:37:18.273161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0145` n `12`; crypto_alt avg `-0.2103` n `228`; crypto_major avg `-0.1915` n `8`; equity avg `0.0807` n `67`; fx avg `-0.0011` n `6`; index avg `0.0134` n `23`; metal avg `-0.0559` n `18`; unknown avg `0.3203` n `419`
- 1h: commodity avg `0.0046` n `12`; crypto_alt avg `-0.3677` n `228`; crypto_major avg `-0.0608` n `8`; equity avg `0.1443` n `67`; fx avg `-0.0013` n `6`; index avg `0.0919` n `23`; metal avg `-0.0035` n `18`; unknown avg `0.3344` n `419`
- 4h: commodity avg `-0.417` n `12`; crypto_alt avg `-0.3101` n `228`; crypto_major avg `0.0387` n `8`; equity avg `0.3668` n `67`; fx avg `0.0241` n `6`; index avg `0.1528` n `23`; metal avg `-0.0281` n `18`; unknown avg `0.1135` n `418`
- 24h: commodity avg `-1.2431` n `12`; crypto_alt avg `-0.3866` n `228`; crypto_major avg `-0.082` n `8`; equity avg `0.0804` n `67`; fx avg `-0.0813` n `6`; index avg `-0.44` n `23`; metal avg `-1.3214` n `18`; unknown avg `-0.293` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1715`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
