# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T19:52:36.192838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `13`; crypto_alt avg `0.6618` n `234`; crypto_major avg `0.3271` n `8`; equity avg `0.1371` n `142`; fx avg `-0.0011` n `6`; index avg `0.0379` n `26`; metal avg `0.0213` n `20`; unknown avg `207.14` n `975`
- 1h: commodity avg `0.0547` n `13`; crypto_alt avg `0.1356` n `234`; crypto_major avg `0.0279` n `8`; equity avg `0.082` n `142`; fx avg `0.0016` n `6`; index avg `0.0385` n `26`; metal avg `0.0691` n `20`; unknown avg `44.4847` n `973`
- 4h: commodity avg `0.0326` n `13`; crypto_alt avg `0.7314` n `234`; crypto_major avg `0.4853` n `8`; equity avg `1.1995` n `142`; fx avg `0.0141` n `6`; index avg `0.2874` n `26`; metal avg `0.211` n `20`; unknown avg `2.0853` n `967`
- 24h: commodity avg `0.0544` n `13`; crypto_alt avg `0.5515` n `234`; crypto_major avg `0.5649` n `8`; equity avg `1.0729` n `142`; fx avg `-0.0875` n `6`; index avg `0.2178` n `26`; metal avg `0.0171` n `20`; unknown avg `0.7451` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
