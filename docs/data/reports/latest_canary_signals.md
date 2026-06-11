# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T02:52:27.371921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0323` n `12`; crypto_alt avg `-0.0311` n `228`; crypto_major avg `0.0355` n `8`; equity avg `0.1349` n `74`; fx avg `-0.0102` n `6`; index avg `0.0202` n `23`; metal avg `-0.2448` n `18`; unknown avg `0.1149` n `550`
- 1h: commodity avg `0.0111` n `12`; crypto_alt avg `-0.6068` n `228`; crypto_major avg `-0.6209` n `8`; equity avg `-0.5958` n `74`; fx avg `-0.0162` n `6`; index avg `-0.203` n `23`; metal avg `-0.9414` n `18`; unknown avg `-0.0792` n `550`
- 4h: commodity avg `-0.2877` n `12`; crypto_alt avg `1.5117` n `228`; crypto_major avg `1.1834` n `8`; equity avg `0.7417` n `74`; fx avg `0.146` n `6`; index avg `0.3768` n `23`; metal avg `0.1447` n `18`; unknown avg `0.5236` n `550`
- 24h: commodity avg `1.4362` n `12`; crypto_alt avg `-0.1457` n `228`; crypto_major avg `-0.1321` n `8`; equity avg `-1.2564` n `74`; fx avg `0.0655` n `6`; index avg `-1.2148` n `23`; metal avg `-1.0491` n `18`; unknown avg `0.0549` n `537`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
