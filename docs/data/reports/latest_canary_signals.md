# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T18:52:27.661111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `0.2028` n `232`; crypto_major avg `0.2119` n `8`; equity avg `0.0112` n `134`; fx avg `-0.0037` n `6`; index avg `0.0026` n `26`; metal avg `0.0018` n `20`; unknown avg `0.8377` n `796`
- 1h: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.1497` n `232`; crypto_major avg `-0.1228` n `8`; equity avg `-0.0197` n `134`; fx avg `-0.0124` n `6`; index avg `0.0048` n `26`; metal avg `-0.0039` n `20`; unknown avg `1.2587` n `774`
- 4h: commodity avg `-0.0497` n `12`; crypto_alt avg `-0.7245` n `232`; crypto_major avg `-0.4025` n `8`; equity avg `0.0717` n `134`; fx avg `-0.0213` n `6`; index avg `0.0412` n `26`; metal avg `-0.0333` n `20`; unknown avg `-0.5898` n `768`
- 24h: commodity avg `0.1619` n `12`; crypto_alt avg `0.1756` n `232`; crypto_major avg `-0.9049` n `8`; equity avg `0.4337` n `134`; fx avg `-0.1231` n `6`; index avg `0.0823` n `26`; metal avg `0.0001` n `20`; unknown avg `156.3011` n `661`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
