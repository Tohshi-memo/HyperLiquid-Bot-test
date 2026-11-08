# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T05:37:23.210479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `13`; crypto_alt avg `0.0389` n `239`; crypto_major avg `0.0091` n `8`; equity avg `0.0219` n `158`; fx avg `0.0068` n `6`; index avg `-0.0032` n `27`; metal avg `0.0` n `20`; unknown avg `-0.217` n `1258`
- 1h: commodity avg `-0.0119` n `13`; crypto_alt avg `0.05` n `239`; crypto_major avg `0.0031` n `8`; equity avg `0.0674` n `158`; fx avg `0.0012` n `6`; index avg `-0.004` n `27`; metal avg `0.0023` n `20`; unknown avg `3.8969` n `1252`
- 4h: commodity avg `-0.0011` n `13`; crypto_alt avg `-0.1934` n `239`; crypto_major avg `-0.0283` n `8`; equity avg `0.0309` n `158`; fx avg `0.0168` n `6`; index avg `-0.0166` n `27`; metal avg `-0.0214` n `20`; unknown avg `-0.45` n `1238`
- 24h: commodity avg `0.1269` n `13`; crypto_alt avg `-1.7814` n `239`; crypto_major avg `-0.6028` n `8`; equity avg `-0.0773` n `158`; fx avg `0.0222` n `6`; index avg `0.0282` n `27`; metal avg `-0.0565` n `20`; unknown avg `162.4883` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
