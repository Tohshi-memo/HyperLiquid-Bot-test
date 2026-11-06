# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T06:52:30.638628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0738` n `13`; crypto_alt avg `-0.168` n `239`; crypto_major avg `-0.2438` n `8`; equity avg `-0.0102` n `158`; fx avg `-0.0174` n `6`; index avg `0.0135` n `27`; metal avg `-0.0088` n `20`; unknown avg `159.0999` n `1256`
- 1h: commodity avg `0.0245` n `13`; crypto_alt avg `0.1963` n `239`; crypto_major avg `-0.0533` n `8`; equity avg `0.0262` n `158`; fx avg `-0.0742` n `6`; index avg `-0.0275` n `27`; metal avg `0.0437` n `20`; unknown avg `-0.222` n `1228`
- 4h: commodity avg `0.0118` n `13`; crypto_alt avg `-0.1251` n `239`; crypto_major avg `-0.9181` n `8`; equity avg `-0.9951` n `158`; fx avg `-0.0646` n `6`; index avg `-0.1534` n `27`; metal avg `-0.2259` n `20`; unknown avg `-0.1715` n `1218`
- 24h: commodity avg `1.4409` n `13`; crypto_alt avg `-4.3037` n `239`; crypto_major avg `-5.9522` n `8`; equity avg `-6.0845` n `158`; fx avg `0.0011` n `6`; index avg `-0.7761` n `27`; metal avg `-0.4984` n `20`; unknown avg `231.7574` n `1031`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
