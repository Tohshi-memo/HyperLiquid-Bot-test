# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T18:07:27.421096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0281` n `12`; crypto_alt avg `0.1274` n `233`; crypto_major avg `0.1094` n `8`; equity avg `0.0234` n `134`; fx avg `-0.0301` n `6`; index avg `0.0075` n `26`; metal avg `0.0018` n `20`; unknown avg `1.2381` n `795`
- 1h: commodity avg `0.0823` n `12`; crypto_alt avg `-0.335` n `233`; crypto_major avg `-0.1535` n `8`; equity avg `-0.0386` n `134`; fx avg `-0.0227` n `6`; index avg `0.0053` n `26`; metal avg `-0.0564` n `20`; unknown avg `0.7063` n `795`
- 4h: commodity avg `-0.2295` n `12`; crypto_alt avg `1.0643` n `232`; crypto_major avg `1.243` n `8`; equity avg `0.9706` n `134`; fx avg `-0.0006` n `6`; index avg `0.0926` n `26`; metal avg `-0.042` n `20`; unknown avg `0.4361` n `765`
- 24h: commodity avg `-0.3093` n `12`; crypto_alt avg `0.5308` n `232`; crypto_major avg `0.3497` n `8`; equity avg `0.9582` n `134`; fx avg `-0.0871` n `6`; index avg `-0.0432` n `26`; metal avg `-0.0361` n `20`; unknown avg `8.8323` n `706`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
