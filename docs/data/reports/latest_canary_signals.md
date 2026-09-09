# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T20:37:34.542839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0396` n `12`; crypto_alt avg `0.2019` n `233`; crypto_major avg `0.1532` n `8`; equity avg `-0.0005` n `134`; fx avg `-0.0029` n `6`; index avg `0.0052` n `26`; metal avg `0.0312` n `20`; unknown avg `1.8958` n `775`
- 1h: commodity avg `0.0364` n `12`; crypto_alt avg `-0.3887` n `233`; crypto_major avg `-0.4265` n `8`; equity avg `-0.1342` n `134`; fx avg `0.0033` n `6`; index avg `-0.0178` n `26`; metal avg `-0.006` n `20`; unknown avg `20.7878` n `745`
- 4h: commodity avg `-0.0109` n `12`; crypto_alt avg `-1.0376` n `233`; crypto_major avg `-0.9637` n `8`; equity avg `-0.2578` n `134`; fx avg `0.0141` n `6`; index avg `0.0189` n `26`; metal avg `-0.0641` n `20`; unknown avg `1.0315` n `745`
- 24h: commodity avg `0.0743` n `12`; crypto_alt avg `-1.2494` n `233`; crypto_major avg `-0.8295` n `8`; equity avg `-0.3334` n `134`; fx avg `-0.0295` n `6`; index avg `-0.121` n `26`; metal avg `0.5113` n `20`; unknown avg `151.3105` n `705`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
