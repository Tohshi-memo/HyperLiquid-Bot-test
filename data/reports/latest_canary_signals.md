# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T00:07:31.824607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0451` n `13`; crypto_alt avg `0.4811` n `239`; crypto_major avg `0.368` n `8`; equity avg `1.0574` n `158`; fx avg `0.0103` n `6`; index avg `0.1552` n `27`; metal avg `0.0955` n `20`; unknown avg `1.0275` n `1244`
- 1h: commodity avg `-0.0767` n `13`; crypto_alt avg `0.4993` n `239`; crypto_major avg `0.4667` n `8`; equity avg `0.415` n `158`; fx avg `0.0128` n `6`; index avg `0.1022` n `27`; metal avg `0.079` n `20`; unknown avg `54.5953` n `1246`
- 4h: commodity avg `0.0398` n `13`; crypto_alt avg `-1.2422` n `239`; crypto_major avg `-0.6866` n `8`; equity avg `-1.0997` n `158`; fx avg `-0.0167` n `6`; index avg `-0.1885` n `27`; metal avg `-0.1335` n `20`; unknown avg `24.6461` n `1178`
- 24h: commodity avg `0.8868` n `13`; crypto_alt avg `-5.1034` n `239`; crypto_major avg `-5.5796` n `8`; equity avg `-8.1074` n `158`; fx avg `0.0683` n `6`; index avg `-1.1603` n `27`; metal avg `0.1192` n `20`; unknown avg `232.4491` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.235`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1905`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1786`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1768`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.167`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1617`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1614`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.16`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1585`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1239`, n `669`, weak_sample_signal
