# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T08:52:27.265445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0362` n `12`; crypto_alt avg `-0.0577` n `232`; crypto_major avg `-0.1105` n `8`; equity avg `-0.0272` n `134`; fx avg `0.0131` n `6`; index avg `-0.0057` n `26`; metal avg `-0.0252` n `20`; unknown avg `0.1352` n `797`
- 1h: commodity avg `0.0743` n `11`; crypto_alt avg `0.1756` n `232`; crypto_major avg `0.1682` n `8`; equity avg `-0.3345` n `123`; fx avg `0.0428` n `5`; index avg `-0.0599` n `20`; metal avg `-0.0217` n `18`; unknown avg `0.2889` n `785`
- 4h: commodity avg `0.2926` n `12`; crypto_alt avg `-0.0719` n `232`; crypto_major avg `-0.118` n `8`; equity avg `-1.2895` n `134`; fx avg `0.0653` n `6`; index avg `-0.3125` n `26`; metal avg `-0.3066` n `20`; unknown avg `0.4398` n `755`
- 24h: commodity avg `0.6129` n `12`; crypto_alt avg `0.562` n `232`; crypto_major avg `-0.8046` n `8`; equity avg `-0.6929` n `134`; fx avg `-0.0569` n `6`; index avg `-0.1881` n `26`; metal avg `-0.033` n `20`; unknown avg `7507.6081` n `666`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
