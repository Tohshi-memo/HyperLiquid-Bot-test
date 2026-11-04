# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T14:22:37.121435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1175` n `13`; crypto_alt avg `0.1418` n `239`; crypto_major avg `0.1656` n `8`; equity avg `0.1986` n `158`; fx avg `-0.0054` n `6`; index avg `0.044` n `27`; metal avg `-0.0171` n `20`; unknown avg `-0.1196` n `1264`
- 1h: commodity avg `-0.3469` n `13`; crypto_alt avg `-0.0632` n `239`; crypto_major avg `0.071` n `8`; equity avg `0.269` n `158`; fx avg `-0.0045` n `6`; index avg `0.0398` n `27`; metal avg `0.0106` n `20`; unknown avg `-0.1558` n `1258`
- 4h: commodity avg `-0.4046` n `13`; crypto_alt avg `-0.6982` n `239`; crypto_major avg `-0.5292` n `8`; equity avg `-1.7571` n `158`; fx avg `0.0215` n `6`; index avg `-0.0632` n `27`; metal avg `-0.1723` n `20`; unknown avg `0.5032` n `1254`
- 24h: commodity avg `-0.4386` n `13`; crypto_alt avg `0.7183` n `239`; crypto_major avg `0.2406` n `8`; equity avg `0.308` n `158`; fx avg `0.1702` n `6`; index avg `0.0996` n `27`; metal avg `0.6622` n `20`; unknown avg `-0.1989` n `1089`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2571`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
