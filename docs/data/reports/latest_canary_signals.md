# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T20:07:29.348997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0276` n `13`; crypto_alt avg `0.3071` n `239`; crypto_major avg `0.2206` n `8`; equity avg `0.3297` n `158`; fx avg `0.0055` n `6`; index avg `0.0285` n `27`; metal avg `0.0421` n `20`; unknown avg `57.6246` n `1237`
- 1h: commodity avg `0.1626` n `13`; crypto_alt avg `0.1349` n `239`; crypto_major avg `0.1483` n `8`; equity avg `0.3109` n `158`; fx avg `-0.0002` n `6`; index avg `0.0153` n `27`; metal avg `-0.0642` n `20`; unknown avg `15.3701` n `1235`
- 4h: commodity avg `0.4181` n `13`; crypto_alt avg `0.0456` n `239`; crypto_major avg `0.1561` n `8`; equity avg `0.6299` n `158`; fx avg `0.004` n `6`; index avg `0.0072` n `27`; metal avg `-0.0178` n `20`; unknown avg `90.2363` n `1235`
- 24h: commodity avg `0.2149` n `13`; crypto_alt avg `1.0106` n `239`; crypto_major avg `-0.4073` n `8`; equity avg `1.8398` n `158`; fx avg `-0.1041` n `6`; index avg `0.2014` n `27`; metal avg `-0.1798` n `20`; unknown avg `59.0106` n `1082`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
