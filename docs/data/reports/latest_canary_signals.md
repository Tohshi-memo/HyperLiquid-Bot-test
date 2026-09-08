# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T19:52:31.304626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0765` n `12`; crypto_alt avg `-0.2908` n `233`; crypto_major avg `-0.2958` n `8`; equity avg `-0.181` n `134`; fx avg `0.0061` n `6`; index avg `-0.0381` n `26`; metal avg `-0.0427` n `20`; unknown avg `0.9418` n `797`
- 1h: commodity avg `-0.0848` n `12`; crypto_alt avg `0.0753` n `233`; crypto_major avg `-0.1042` n `8`; equity avg `-0.3126` n `134`; fx avg `-0.0055` n `6`; index avg `-0.0371` n `26`; metal avg `-0.0112` n `20`; unknown avg `11.5843` n `795`
- 4h: commodity avg `0.3031` n `12`; crypto_alt avg `-1.291` n `232`; crypto_major avg `-0.638` n `8`; equity avg `-0.6897` n `134`; fx avg `-0.0404` n `6`; index avg `-0.0942` n `26`; metal avg `-0.2377` n `20`; unknown avg `0.5232` n `765`
- 24h: commodity avg `-0.0003` n `12`; crypto_alt avg `-0.6325` n `232`; crypto_major avg `-0.5683` n `8`; equity avg `0.2159` n `134`; fx avg `-0.0944` n `6`; index avg `-0.1545` n `26`; metal avg `-0.2887` n `20`; unknown avg `10.0419` n `706`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
