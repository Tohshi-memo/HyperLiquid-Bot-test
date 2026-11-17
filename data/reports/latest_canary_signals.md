# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T19:37:24.166030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0551` n `13`; crypto_alt avg `-0.1338` n `239`; crypto_major avg `-0.1796` n `8`; equity avg `-0.1924` n `163`; fx avg `0.006` n `6`; index avg `-0.0234` n `27`; metal avg `-0.0498` n `20`; unknown avg `4.7846` n `1265`
- 1h: commodity avg `-0.1986` n `13`; crypto_alt avg `-0.159` n `239`; crypto_major avg `-0.1766` n `8`; equity avg `-0.2159` n `163`; fx avg `-0.0014` n `6`; index avg `-0.0257` n `27`; metal avg `-0.1048` n `20`; unknown avg `5.2492` n `1263`
- 4h: commodity avg `0.0924` n `13`; crypto_alt avg `-0.9933` n `239`; crypto_major avg `-0.7953` n `8`; equity avg `0.0486` n `163`; fx avg `0.0352` n `6`; index avg `-0.0083` n `27`; metal avg `-0.1654` n `20`; unknown avg `5.0512` n `1245`
- 24h: commodity avg `0.1483` n `13`; crypto_alt avg `-0.5935` n `239`; crypto_major avg `-0.1778` n `8`; equity avg `-1.9924` n `163`; fx avg `0.0358` n `6`; index avg `-0.225` n `27`; metal avg `-0.1002` n `20`; unknown avg `12.4886` n `1099`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
