# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T21:37:32.768900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `13`; crypto_alt avg `-0.0308` n `239`; crypto_major avg `0.0734` n `8`; equity avg `0.0611` n `160`; fx avg `0.0115` n `6`; index avg `0.0003` n `27`; metal avg `-0.022` n `20`; unknown avg `0.6988` n `1262`
- 1h: commodity avg `-0.0351` n `13`; crypto_alt avg `0.3247` n `239`; crypto_major avg `0.4751` n `8`; equity avg `0.539` n `160`; fx avg `-0.0025` n `6`; index avg `0.048` n `27`; metal avg `-0.0221` n `20`; unknown avg `0.9707` n `1240`
- 4h: commodity avg `0.1969` n `13`; crypto_alt avg `0.729` n `239`; crypto_major avg `1.4735` n `8`; equity avg `1.4975` n `160`; fx avg `0.0231` n `6`; index avg `0.1495` n `27`; metal avg `0.1517` n `20`; unknown avg `1.3097` n `1232`
- 24h: commodity avg `0.0869` n `13`; crypto_alt avg `-1.5077` n `239`; crypto_major avg `-2.335` n `8`; equity avg `-1.3073` n `160`; fx avg `-0.0864` n `6`; index avg `-0.1821` n `27`; metal avg `-0.6783` n `20`; unknown avg `20.582` n `1173`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2586`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
