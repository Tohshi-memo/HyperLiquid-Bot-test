# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T00:37:22.431667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0852` n `13`; crypto_alt avg `-0.292` n `239`; crypto_major avg `-0.2347` n `8`; equity avg `-0.0799` n `162`; fx avg `-0.0148` n `6`; index avg `-0.0149` n `27`; metal avg `-0.0497` n `20`; unknown avg `0.0688` n `1265`
- 1h: commodity avg `0.0185` n `13`; crypto_alt avg `-0.6808` n `239`; crypto_major avg `-0.7792` n `8`; equity avg `-0.1629` n `162`; fx avg `-0.026` n `6`; index avg `-0.0527` n `27`; metal avg `-0.0491` n `20`; unknown avg `2.2075` n `1257`
- 4h: commodity avg `-0.2852` n `13`; crypto_alt avg `-0.3291` n `239`; crypto_major avg `-0.1417` n `8`; equity avg `0.8973` n `162`; fx avg `-0.0371` n `6`; index avg `0.1341` n `27`; metal avg `0.2609` n `20`; unknown avg `0.8702` n `1187`
- 24h: commodity avg `-0.2847` n `13`; crypto_alt avg `1.9345` n `239`; crypto_major avg `2.9517` n `8`; equity avg `1.9611` n `162`; fx avg `-0.0117` n `6`; index avg `0.2249` n `27`; metal avg `0.5146` n `20`; unknown avg `2.201` n `1138`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
