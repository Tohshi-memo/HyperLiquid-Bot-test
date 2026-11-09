# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T13:22:26.073578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0821` n `13`; crypto_alt avg `-0.1791` n `239`; crypto_major avg `-0.2483` n `8`; equity avg `-0.3773` n `158`; fx avg `0.0019` n `6`; index avg `-0.0376` n `27`; metal avg `-0.012` n `20`; unknown avg `0.0963` n `1263`
- 1h: commodity avg `0.1291` n `13`; crypto_alt avg `0.3818` n `239`; crypto_major avg `-0.0007` n `8`; equity avg `0.1984` n `158`; fx avg `0.0244` n `6`; index avg `0.0184` n `27`; metal avg `0.0354` n `20`; unknown avg `19.0472` n `1257`
- 4h: commodity avg `-0.3164` n `13`; crypto_alt avg `1.6512` n `239`; crypto_major avg `0.2388` n `8`; equity avg `0.8256` n `158`; fx avg `-0.0292` n `6`; index avg `0.1044` n `27`; metal avg `0.1272` n `20`; unknown avg `0.4187` n `1251`
- 24h: commodity avg `-0.3296` n `13`; crypto_alt avg `-0.4682` n `239`; crypto_major avg `-3.5573` n `8`; equity avg `-0.0757` n `158`; fx avg `-0.1333` n `6`; index avg `0.0207` n `27`; metal avg `0.369` n `20`; unknown avg `0.8081` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
