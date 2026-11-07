# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T17:07:25.032581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0216` n `13`; crypto_alt avg `0.0746` n `239`; crypto_major avg `0.0525` n `8`; equity avg `0.0391` n `158`; fx avg `0.0009` n `6`; index avg `0.015` n `27`; metal avg `0.0033` n `20`; unknown avg `-0.2221` n `1257`
- 1h: commodity avg `0.0502` n `13`; crypto_alt avg `0.0584` n `239`; crypto_major avg `-0.0222` n `8`; equity avg `0.0032` n `158`; fx avg `0.011` n `6`; index avg `-0.0044` n `27`; metal avg `-0.0075` n `20`; unknown avg `-0.5709` n `1255`
- 4h: commodity avg `0.1038` n `13`; crypto_alt avg `-0.2814` n `239`; crypto_major avg `-0.1391` n `8`; equity avg `-0.2061` n `158`; fx avg `-0.0352` n `6`; index avg `0.0227` n `27`; metal avg `-0.0231` n `20`; unknown avg `160.5267` n `1241`
- 24h: commodity avg `0.3059` n `13`; crypto_alt avg `-1.9548` n `239`; crypto_major avg `-1.0549` n `8`; equity avg `0.0649` n `158`; fx avg `0.004` n `6`; index avg `-0.0115` n `27`; metal avg `0.0364` n `20`; unknown avg `-0.9113` n `1109`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
