# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T14:07:41.299835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `13`; crypto_alt avg `0.1573` n `239`; crypto_major avg `0.1216` n `8`; equity avg `0.2556` n `162`; fx avg `0.0198` n `6`; index avg `0.023` n `27`; metal avg `0.065` n `20`; unknown avg `158.9068` n `1260`
- 1h: commodity avg `0.0125` n `13`; crypto_alt avg `-0.2494` n `239`; crypto_major avg `-0.1701` n `8`; equity avg `-0.2588` n `162`; fx avg `0.0061` n `6`; index avg `-0.0348` n `27`; metal avg `-0.1015` n `20`; unknown avg `1.629` n `1224`
- 4h: commodity avg `0.1935` n `13`; crypto_alt avg `1.1239` n `239`; crypto_major avg `1.0862` n `8`; equity avg `1.4534` n `162`; fx avg `0.0365` n `6`; index avg `0.1046` n `27`; metal avg `0.0536` n `20`; unknown avg `2.0859` n `1218`
- 24h: commodity avg `-0.3132` n `13`; crypto_alt avg `1.9122` n `239`; crypto_major avg `2.3029` n `8`; equity avg `-0.9998` n `162`; fx avg `-0.0527` n `6`; index avg `-0.1527` n `27`; metal avg `-0.138` n `20`; unknown avg `4.7388` n `1103`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.168`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
