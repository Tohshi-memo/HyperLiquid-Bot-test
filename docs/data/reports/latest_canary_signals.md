# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T15:22:13.848068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0559` n `12`; crypto_alt avg `0.0621` n `228`; crypto_major avg `0.0183` n `8`; equity avg `-0.0113` n `74`; fx avg `0.0179` n `6`; index avg `0.068` n `23`; metal avg `-0.0073` n `18`; unknown avg `0.0875` n `645`
- 1h: commodity avg `-0.202` n `12`; crypto_alt avg `-0.3321` n `228`; crypto_major avg `-0.2252` n `8`; equity avg `0.0932` n `74`; fx avg `-0.0193` n `6`; index avg `0.099` n `23`; metal avg `0.0326` n `18`; unknown avg `0.0048` n `645`
- 4h: commodity avg `0.3655` n `12`; crypto_alt avg `-0.7237` n `228`; crypto_major avg `-0.6548` n `8`; equity avg `-0.248` n `74`; fx avg `-0.0099` n `6`; index avg `0.104` n `23`; metal avg `-0.0679` n `18`; unknown avg `0.0622` n `645`
- 24h: commodity avg `-0.0615` n `12`; crypto_alt avg `-1.8456` n `228`; crypto_major avg `-1.0833` n `8`; equity avg `0.3573` n `74`; fx avg `-0.0215` n `6`; index avg `0.1682` n `23`; metal avg `-0.0113` n `18`; unknown avg `1.3298` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
