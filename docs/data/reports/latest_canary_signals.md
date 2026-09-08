# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T17:07:25.826263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0634` n `12`; crypto_alt avg `0.0599` n `233`; crypto_major avg `0.0352` n `8`; equity avg `0.1143` n `134`; fx avg `0.0015` n `6`; index avg `0.0338` n `26`; metal avg `0.0695` n `20`; unknown avg `0.376` n `795`
- 1h: commodity avg `-0.0183` n `12`; crypto_alt avg `-0.0424` n `233`; crypto_major avg `0.1092` n `8`; equity avg `0.0173` n `134`; fx avg `0.0017` n `6`; index avg `0.0018` n `26`; metal avg `0.0923` n `20`; unknown avg `-0.1218` n `765`
- 4h: commodity avg `-0.3758` n `12`; crypto_alt avg `0.786` n `232`; crypto_major avg `0.9945` n `8`; equity avg `0.9395` n `134`; fx avg `0.0328` n `6`; index avg `-0.018` n `26`; metal avg `-0.0845` n `20`; unknown avg `-0.1371` n `759`
- 24h: commodity avg `-0.3082` n `12`; crypto_alt avg `0.8708` n `232`; crypto_major avg `0.5177` n `8`; equity avg `1.0861` n `134`; fx avg `-0.0652` n `6`; index avg `-0.0418` n `26`; metal avg `-0.0012` n `20`; unknown avg `7061.3831` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
