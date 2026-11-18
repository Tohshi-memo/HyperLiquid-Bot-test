# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T02:52:26.737321+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0263` n `13`; crypto_alt avg `-0.2259` n `239`; crypto_major avg `-0.28` n `8`; equity avg `-0.425` n `163`; fx avg `-0.0063` n `6`; index avg `-0.0631` n `27`; metal avg `-0.0481` n `20`; unknown avg `1.0759` n `1266`
- 1h: commodity avg `-0.0578` n `13`; crypto_alt avg `-0.314` n `239`; crypto_major avg `-0.2432` n `8`; equity avg `-0.6003` n `163`; fx avg `-0.0245` n `6`; index avg `-0.0583` n `27`; metal avg `-0.2291` n `20`; unknown avg `9.2496` n `1264`
- 4h: commodity avg `-0.1841` n `13`; crypto_alt avg `-0.686` n `239`; crypto_major avg `-0.4174` n `8`; equity avg `-1.4586` n `163`; fx avg `-0.1144` n `6`; index avg `-0.2116` n `27`; metal avg `-0.526` n `20`; unknown avg `45.0854` n `1255`
- 24h: commodity avg `0.2236` n `13`; crypto_alt avg `0.2013` n `239`; crypto_major avg `0.5355` n `8`; equity avg `-0.7634` n `163`; fx avg `-0.1178` n `6`; index avg `-0.1776` n `27`; metal avg `-0.7091` n `20`; unknown avg `6.9828` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
