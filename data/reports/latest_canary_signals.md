# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T03:37:33.999046+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `13`; crypto_alt avg `-0.1307` n `234`; crypto_major avg `-0.029` n `8`; equity avg `-0.0378` n `142`; fx avg `-0.0025` n `6`; index avg `0.0012` n `26`; metal avg `0.0147` n `20`; unknown avg `-0.0317` n `985`
- 1h: commodity avg `-0.0255` n `13`; crypto_alt avg `0.0117` n `234`; crypto_major avg `0.3065` n `8`; equity avg `0.0466` n `142`; fx avg `0.007` n `6`; index avg `0.0128` n `26`; metal avg `0.1299` n `20`; unknown avg `0.7267` n `983`
- 4h: commodity avg `-0.132` n `13`; crypto_alt avg `0.553` n `234`; crypto_major avg `0.5851` n `8`; equity avg `0.0968` n `142`; fx avg `-0.0039` n `6`; index avg `0.0656` n `26`; metal avg `-0.0336` n `20`; unknown avg `0.5862` n `977`
- 24h: commodity avg `0.4208` n `13`; crypto_alt avg `-0.7046` n `234`; crypto_major avg `0.5188` n `8`; equity avg `0.6291` n `142`; fx avg `-0.2235` n `6`; index avg `0.0893` n `26`; metal avg `-0.0578` n `20`; unknown avg `0.3186` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
