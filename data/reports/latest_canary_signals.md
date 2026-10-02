# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T03:22:27.068382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `13`; crypto_alt avg `-0.1243` n `234`; crypto_major avg `-0.0384` n `8`; equity avg `-0.0058` n `142`; fx avg `-0.0006` n `6`; index avg `0.0019` n `26`; metal avg `0.0065` n `20`; unknown avg `0.4124` n `985`
- 1h: commodity avg `-0.0445` n `13`; crypto_alt avg `0.1623` n `234`; crypto_major avg `0.3642` n `8`; equity avg `0.0902` n `142`; fx avg `0.0185` n `6`; index avg `0.014` n `26`; metal avg `0.1126` n `20`; unknown avg `1.8323` n `983`
- 4h: commodity avg `-0.1646` n `13`; crypto_alt avg `0.7527` n `234`; crypto_major avg `0.6648` n `8`; equity avg `0.1189` n `142`; fx avg `-0.0067` n `6`; index avg `0.0405` n `26`; metal avg `-0.0504` n `20`; unknown avg `0.7678` n `977`
- 24h: commodity avg `0.0385` n `13`; crypto_alt avg `-0.2778` n `234`; crypto_major avg `0.7122` n `8`; equity avg `0.6697` n `142`; fx avg `-0.2131` n `6`; index avg `0.0803` n `26`; metal avg `-0.0832` n `20`; unknown avg `0.283` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
