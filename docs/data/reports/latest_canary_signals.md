# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T03:37:30.710832+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `13`; crypto_alt avg `-0.0378` n `239`; crypto_major avg `-0.0563` n `8`; equity avg `-0.0215` n `158`; fx avg `-0.0016` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0094` n `20`; unknown avg `0.418` n `1262`
- 1h: commodity avg `-0.0177` n `13`; crypto_alt avg `0.0755` n `239`; crypto_major avg `0.109` n `8`; equity avg `0.1072` n `158`; fx avg `0.0091` n `6`; index avg `0.0165` n `27`; metal avg `-0.0023` n `20`; unknown avg `1.9026` n `1254`
- 4h: commodity avg `-0.044` n `13`; crypto_alt avg `-0.5715` n `239`; crypto_major avg `-0.1128` n `8`; equity avg `0.0199` n `158`; fx avg `0.0392` n `6`; index avg `0.0084` n `27`; metal avg `-0.0214` n `20`; unknown avg `0.5451` n `1246`
- 24h: commodity avg `0.1225` n `13`; crypto_alt avg `-1.3576` n `239`; crypto_major avg `-0.4855` n `8`; equity avg `-0.0699` n `158`; fx avg `0.026` n `6`; index avg `0.0472` n `27`; metal avg `-0.0536` n `20`; unknown avg `161.1456` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
