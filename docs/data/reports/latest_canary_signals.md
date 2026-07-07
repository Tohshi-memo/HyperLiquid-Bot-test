# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T00:37:25.315627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `-0.0399` n `229`; crypto_major avg `0.0984` n `8`; equity avg `-0.2707` n `91`; fx avg `0.0134` n `6`; index avg `-0.1` n `25`; metal avg `-0.0921` n `20`; unknown avg `-0.0743` n `763`
- 1h: commodity avg `0.0372` n `12`; crypto_alt avg `-0.0147` n `229`; crypto_major avg `0.0931` n `8`; equity avg `-0.4708` n `91`; fx avg `0.0136` n `6`; index avg `-0.1744` n `25`; metal avg `-0.1424` n `20`; unknown avg `-0.0351` n `763`
- 4h: commodity avg `0.0802` n `12`; crypto_alt avg `0.2015` n `229`; crypto_major avg `0.2214` n `8`; equity avg `-0.8587` n `91`; fx avg `0.0236` n `6`; index avg `-0.2278` n `25`; metal avg `-0.155` n `20`; unknown avg `1.3613` n `763`
- 24h: commodity avg `0.3341` n `12`; crypto_alt avg `0.8329` n `229`; crypto_major avg `0.1597` n `8`; equity avg `-1.2695` n `90`; fx avg `0.1156` n `6`; index avg `-0.2553` n `25`; metal avg `-0.4123` n `20`; unknown avg `-0.2286` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
