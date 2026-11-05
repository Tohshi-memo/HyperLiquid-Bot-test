# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T03:44:02.926342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0805` n `13`; crypto_alt avg `-0.0064` n `239`; crypto_major avg `-0.014` n `8`; equity avg `-0.0839` n `158`; fx avg `-0.0024` n `6`; index avg `-0.0226` n `27`; metal avg `0.0035` n `20`; unknown avg `-0.564` n `1261`
- 1h: commodity avg `-0.2002` n `13`; crypto_alt avg `0.4726` n `239`; crypto_major avg `0.2441` n `8`; equity avg `-0.2777` n `158`; fx avg `-0.0046` n `6`; index avg `-0.0582` n `27`; metal avg `0.1093` n `20`; unknown avg `-0.4223` n `1255`
- 4h: commodity avg `-0.3446` n `13`; crypto_alt avg `0.6251` n `239`; crypto_major avg `0.2905` n `8`; equity avg `-0.6727` n `158`; fx avg `0.0362` n `6`; index avg `-0.1932` n `27`; metal avg `0.5101` n `20`; unknown avg `4.5241` n `1246`
- 24h: commodity avg `-1.8003` n `13`; crypto_alt avg `4.65` n `239`; crypto_major avg `4.6256` n `8`; equity avg `1.1619` n `158`; fx avg `0.1499` n `6`; index avg `0.4943` n `27`; metal avg `2.0317` n `20`; unknown avg `34.2493` n `1032`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.251`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1986`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1959`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
