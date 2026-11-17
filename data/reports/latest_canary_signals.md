# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T20:07:33.459196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `13`; crypto_alt avg `-0.0499` n `239`; crypto_major avg `0.0351` n `8`; equity avg `-0.0235` n `163`; fx avg `-0.0158` n `6`; index avg `0.0091` n `27`; metal avg `-0.0327` n `20`; unknown avg `4.9371` n `1251`
- 1h: commodity avg `-0.2794` n `13`; crypto_alt avg `0.4081` n `239`; crypto_major avg `0.2438` n `8`; equity avg `-0.3193` n `163`; fx avg `-0.0261` n `6`; index avg `-0.0399` n `27`; metal avg `-0.0913` n `20`; unknown avg `6.553` n `1253`
- 4h: commodity avg `-0.2375` n `13`; crypto_alt avg `-0.2312` n `239`; crypto_major avg `0.2324` n `8`; equity avg `-0.0867` n `163`; fx avg `-0.0064` n `6`; index avg `-0.0041` n `27`; metal avg `-0.1832` n `20`; unknown avg `6.4967` n `1249`
- 24h: commodity avg `0.0524` n `13`; crypto_alt avg `-0.9193` n `239`; crypto_major avg `-0.6547` n `8`; equity avg `-2.1753` n `163`; fx avg `0.0266` n `6`; index avg `-0.2594` n `27`; metal avg `-0.1683` n `20`; unknown avg `10.1477` n `1099`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
