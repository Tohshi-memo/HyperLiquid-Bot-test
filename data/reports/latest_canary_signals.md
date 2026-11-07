# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T15:07:30.614525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `13`; crypto_alt avg `-0.3776` n `239`; crypto_major avg `-0.1657` n `8`; equity avg `-0.0369` n `158`; fx avg `0.011` n `6`; index avg `0.0009` n `27`; metal avg `-0.0063` n `20`; unknown avg `159.0966` n `1257`
- 1h: commodity avg `0.0098` n `13`; crypto_alt avg `-0.3571` n `239`; crypto_major avg `-0.1678` n `8`; equity avg `-0.0891` n `158`; fx avg `-0.0031` n `6`; index avg `0.0003` n `27`; metal avg `-0.0065` n `20`; unknown avg `159.2782` n `1255`
- 4h: commodity avg `0.0031` n `13`; crypto_alt avg `-0.3304` n `239`; crypto_major avg `-0.3187` n `8`; equity avg `-0.0163` n `158`; fx avg `0.0219` n `6`; index avg `0.0119` n `27`; metal avg `-0.0113` n `20`; unknown avg `-0.0949` n `1249`
- 24h: commodity avg `0.1569` n `13`; crypto_alt avg `-1.8394` n `239`; crypto_major avg `-0.2892` n `8`; equity avg `0.1366` n `158`; fx avg `0.0059` n `6`; index avg `-0.0256` n `27`; metal avg `0.1211` n `20`; unknown avg `-0.3485` n `1117`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
