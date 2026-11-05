# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T00:07:32.281115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `13`; crypto_alt avg `-0.2441` n `239`; crypto_major avg `-0.1554` n `8`; equity avg `-0.3521` n `158`; fx avg `0.0133` n `6`; index avg `-0.0598` n `27`; metal avg `-0.0585` n `20`; unknown avg `0.8448` n `1252`
- 1h: commodity avg `-0.0185` n `13`; crypto_alt avg `-0.5058` n `239`; crypto_major avg `-0.2417` n `8`; equity avg `-0.4905` n `158`; fx avg `-0.0044` n `6`; index avg `-0.1117` n `27`; metal avg `-0.0188` n `20`; unknown avg `0.704` n `1250`
- 4h: commodity avg `-0.0977` n `13`; crypto_alt avg `0.5435` n `239`; crypto_major avg `0.3918` n `8`; equity avg `-0.1776` n `158`; fx avg `0.0106` n `6`; index avg `-0.0477` n `27`; metal avg `-0.0414` n `20`; unknown avg `0.5812` n `1154`
- 24h: commodity avg `-1.8029` n `13`; crypto_alt avg `1.6369` n `239`; crypto_major avg `2.3306` n `8`; equity avg `-1.8363` n `158`; fx avg `0.0344` n `6`; index avg `-0.0171` n `27`; metal avg `1.1433` n `20`; unknown avg `30.5589` n `1036`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2654`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
