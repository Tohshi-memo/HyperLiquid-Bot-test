# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T20:22:24.470553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0653` n `12`; crypto_alt avg `0.621` n `228`; crypto_major avg `0.4342` n `8`; equity avg `0.1217` n `69`; fx avg `0.0083` n `6`; index avg `-0.0527` n `23`; metal avg `0.0491` n `18`; unknown avg `0.3988` n `417`
- 1h: commodity avg `0.0231` n `12`; crypto_alt avg `-0.0937` n `228`; crypto_major avg `-0.0371` n `8`; equity avg `0.2158` n `69`; fx avg `0.0079` n `6`; index avg `-0.0995` n `23`; metal avg `0.0043` n `18`; unknown avg `0.1989` n `417`
- 4h: commodity avg `0.2785` n `12`; crypto_alt avg `0.9821` n `228`; crypto_major avg `0.89` n `8`; equity avg `0.5566` n `69`; fx avg `-0.0118` n `6`; index avg `-0.1012` n `23`; metal avg `-0.0788` n `18`; unknown avg `0.3789` n `417`
- 24h: commodity avg `1.0416` n `12`; crypto_alt avg `-3.6371` n `228`; crypto_major avg `-1.3813` n `8`; equity avg `1.6124` n `69`; fx avg `-0.0269` n `6`; index avg `0.7177` n `23`; metal avg `0.4976` n `18`; unknown avg `-0.7648` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
