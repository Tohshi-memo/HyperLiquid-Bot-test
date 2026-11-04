# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T22:52:26.429078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0408` n `13`; crypto_alt avg `0.1194` n `239`; crypto_major avg `0.0862` n `8`; equity avg `-0.0168` n `158`; fx avg `-0.0028` n `6`; index avg `-0.0029` n `27`; metal avg `-0.0138` n `20`; unknown avg `0.0839` n `1264`
- 1h: commodity avg `0.0213` n `13`; crypto_alt avg `0.9422` n `239`; crypto_major avg `0.8654` n `8`; equity avg `0.024` n `158`; fx avg `-0.0101` n `6`; index avg `0.0305` n `27`; metal avg `-0.0003` n `20`; unknown avg `-1.1496` n `1258`
- 4h: commodity avg `-0.0158` n `13`; crypto_alt avg `0.8569` n `239`; crypto_major avg `0.4449` n `8`; equity avg `0.3773` n `158`; fx avg `0.0106` n `6`; index avg `0.0749` n `27`; metal avg `0.0101` n `20`; unknown avg `166.2241` n `1194`
- 24h: commodity avg `-1.8551` n `13`; crypto_alt avg `2.2501` n `239`; crypto_major avg `2.3691` n `8`; equity avg `-1.4376` n `158`; fx avg `0.0732` n `6`; index avg `0.1107` n `27`; metal avg `1.2284` n `20`; unknown avg `-0.7979` n `1080`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2659`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
