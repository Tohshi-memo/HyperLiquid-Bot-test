# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T13:37:29.620286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0717` n `12`; crypto_alt avg `0.2408` n `230`; crypto_major avg `0.4789` n `8`; equity avg `0.0792` n `102`; fx avg `0.0034` n `6`; index avg `-0.0381` n `25`; metal avg `-0.0157` n `20`; unknown avg `0.1479` n `774`
- 1h: commodity avg `0.0434` n `12`; crypto_alt avg `0.252` n `230`; crypto_major avg `0.5715` n `8`; equity avg `0.0323` n `102`; fx avg `0.0106` n `6`; index avg `-0.0373` n `25`; metal avg `-0.0079` n `20`; unknown avg `0.2696` n `774`
- 4h: commodity avg `0.3552` n `12`; crypto_alt avg `-0.0492` n `230`; crypto_major avg `0.1246` n `8`; equity avg `-0.4624` n `102`; fx avg `-0.0115` n `6`; index avg `-0.1194` n `25`; metal avg `-0.0875` n `20`; unknown avg `0.0367` n `773`
- 24h: commodity avg `-0.455` n `12`; crypto_alt avg `0.6821` n `230`; crypto_major avg `1.5739` n `8`; equity avg `0.7959` n `102`; fx avg `0.0875` n `6`; index avg `0.0478` n `25`; metal avg `0.2429` n `20`; unknown avg `-0.044` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
