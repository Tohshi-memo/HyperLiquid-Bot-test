# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T21:04:23.353157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2492` n `12`; crypto_alt avg `0.0085` n `228`; crypto_major avg `-0.0249` n `8`; equity avg `0.0137` n `69`; fx avg `-0.0021` n `6`; index avg `-0.0323` n `23`; metal avg `-0.0638` n `18`; unknown avg `-0.0277` n `419`
- 1h: commodity avg `0.2188` n `12`; crypto_alt avg `0.0485` n `228`; crypto_major avg `-0.0892` n `8`; equity avg `-0.0396` n `69`; fx avg `-0.0397` n `6`; index avg `-0.0662` n `23`; metal avg `-0.1803` n `18`; unknown avg `-0.1758` n `419`
- 4h: commodity avg `0.3818` n `12`; crypto_alt avg `-0.5177` n `228`; crypto_major avg `-0.6336` n `8`; equity avg `0.0283` n `69`; fx avg `-0.0167` n `6`; index avg `-0.0979` n `23`; metal avg `-0.3814` n `18`; unknown avg `-0.3054` n `419`
- 24h: commodity avg `-0.5585` n `12`; crypto_alt avg `0.5552` n `228`; crypto_major avg `1.0165` n `8`; equity avg `1.3192` n `69`; fx avg `0.182` n `6`; index avg `0.1062` n `23`; metal avg `-0.0169` n `18`; unknown avg `0.5599` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
