# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T15:22:27.271607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `0.2005` n `232`; crypto_major avg `0.018` n `8`; equity avg `0.2086` n `134`; fx avg `-0.0037` n `6`; index avg `0.0279` n `26`; metal avg `-0.0206` n `20`; unknown avg `1.0854` n `797`
- 1h: commodity avg `-0.0976` n `12`; crypto_alt avg `0.6215` n `232`; crypto_major avg `0.2539` n `8`; equity avg `0.5229` n `134`; fx avg `0.03` n `6`; index avg `0.0717` n `26`; metal avg `0.024` n `20`; unknown avg `1.3695` n `795`
- 4h: commodity avg `-0.4121` n `12`; crypto_alt avg `0.4163` n `232`; crypto_major avg `0.2469` n `8`; equity avg `1.0063` n `134`; fx avg `0.0311` n `6`; index avg `0.0539` n `26`; metal avg `0.0018` n `20`; unknown avg `0.0165` n `775`
- 24h: commodity avg `-0.1967` n `12`; crypto_alt avg `0.4618` n `232`; crypto_major avg `-0.2633` n `8`; equity avg `0.9664` n `134`; fx avg `-0.0529` n `6`; index avg `0.0112` n `26`; metal avg `-0.0103` n `20`; unknown avg `7062.369` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
