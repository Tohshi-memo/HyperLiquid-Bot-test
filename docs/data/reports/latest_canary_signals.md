# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T12:52:29.359859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1584` n `13`; crypto_alt avg `-0.1573` n `239`; crypto_major avg `-0.1176` n `8`; equity avg `-0.7424` n `158`; fx avg `0.0127` n `6`; index avg `-0.0537` n `27`; metal avg `-0.0155` n `20`; unknown avg `0.7116` n `1264`
- 1h: commodity avg `0.1224` n `13`; crypto_alt avg `-0.8653` n `239`; crypto_major avg `-0.96` n `8`; equity avg `-1.7776` n `158`; fx avg `0.0036` n `6`; index avg `-0.1372` n `27`; metal avg `-0.0036` n `20`; unknown avg `1.2609` n `1252`
- 4h: commodity avg `-0.2281` n `13`; crypto_alt avg `-0.7468` n `239`; crypto_major avg `-0.699` n `8`; equity avg `-1.2638` n `158`; fx avg `0.0449` n `6`; index avg `0.0195` n `27`; metal avg `0.0877` n `20`; unknown avg `3.8172` n `1230`
- 24h: commodity avg `-0.2961` n `13`; crypto_alt avg `0.3642` n `239`; crypto_major avg `-0.1092` n `8`; equity avg `0.1849` n `158`; fx avg `0.1771` n `6`; index avg `0.0826` n `27`; metal avg `0.8367` n `20`; unknown avg `-0.1051` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2505`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
