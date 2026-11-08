# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T04:07:30.907360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `0.0508` n `239`; crypto_major avg `0.0711` n `8`; equity avg `0.0033` n `158`; fx avg `0.0015` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0007` n `20`; unknown avg `-0.2057` n `1252`
- 1h: commodity avg `-0.0238` n `13`; crypto_alt avg `-0.0385` n `239`; crypto_major avg `0.0381` n `8`; equity avg `-0.0627` n `158`; fx avg `0.0021` n `6`; index avg `-0.0009` n `27`; metal avg `-0.0083` n `20`; unknown avg `7.3483` n `1250`
- 4h: commodity avg `0.0078` n `13`; crypto_alt avg `-0.5579` n `239`; crypto_major avg `-0.1033` n `8`; equity avg `-0.0679` n `158`; fx avg `0.0198` n `6`; index avg `-0.0156` n `27`; metal avg `-0.0177` n `20`; unknown avg `-0.2675` n `1246`
- 24h: commodity avg `0.1438` n `13`; crypto_alt avg `-1.5161` n `239`; crypto_major avg `-0.4632` n `8`; equity avg `-0.0981` n `158`; fx avg `0.0068` n `6`; index avg `0.0394` n `27`; metal avg `-0.0484` n `20`; unknown avg `160.8567` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
