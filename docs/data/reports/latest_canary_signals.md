# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T20:52:31.048267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `12`; crypto_alt avg `-0.0094` n `233`; crypto_major avg `0.0506` n `8`; equity avg `0.01` n `134`; fx avg `-0.0048` n `6`; index avg `0.0015` n `26`; metal avg `-0.0125` n `20`; unknown avg `1.7806` n `797`
- 1h: commodity avg `0.0829` n `12`; crypto_alt avg `0.0568` n `233`; crypto_major avg `0.2461` n `8`; equity avg `0.0729` n `134`; fx avg `-0.0107` n `6`; index avg `-0.0165` n `26`; metal avg `-0.0371` n `20`; unknown avg `0.0937` n `765`
- 4h: commodity avg `0.3835` n `12`; crypto_alt avg `-1.1082` n `233`; crypto_major avg `-0.5605` n `8`; equity avg `-0.5363` n `134`; fx avg `-0.0488` n `6`; index avg `-0.0802` n `26`; metal avg `-0.2512` n `20`; unknown avg `0.2325` n `765`
- 24h: commodity avg `0.1128` n `12`; crypto_alt avg `-0.5715` n `232`; crypto_major avg `-0.236` n `8`; equity avg `0.2899` n `134`; fx avg `-0.1094` n `6`; index avg `-0.1712` n `26`; metal avg `-0.3353` n `20`; unknown avg `14.0301` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
