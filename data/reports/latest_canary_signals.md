# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T19:22:35.697781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0443` n `12`; crypto_alt avg `-0.057` n `234`; crypto_major avg `0.0441` n `8`; equity avg `-0.0267` n `140`; fx avg `-0.0001` n `6`; index avg `-0.008` n `26`; metal avg `-0.0459` n `20`; unknown avg `17.9223` n `917`
- 1h: commodity avg `-0.176` n `12`; crypto_alt avg `-0.2595` n `234`; crypto_major avg `-0.251` n `8`; equity avg `-0.0516` n `140`; fx avg `-0.0054` n `6`; index avg `-0.0081` n `26`; metal avg `-0.1039` n `20`; unknown avg `3.769` n `915`
- 4h: commodity avg `-0.0209` n `12`; crypto_alt avg `0.9577` n `234`; crypto_major avg `0.3222` n `8`; equity avg `0.3677` n `140`; fx avg `0.0063` n `6`; index avg `0.0451` n `26`; metal avg `-0.1335` n `20`; unknown avg `2.6181` n `907`
- 24h: commodity avg `-0.2022` n `12`; crypto_alt avg `4.771` n `234`; crypto_major avg `2.3083` n `8`; equity avg `3.5417` n `138`; fx avg `0.0257` n `6`; index avg `0.6688` n `26`; metal avg `0.7628` n `20`; unknown avg `4.5596` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
