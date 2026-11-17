# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T11:22:28.188777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0198` n `13`; crypto_alt avg `0.2086` n `239`; crypto_major avg `0.0695` n `8`; equity avg `0.1687` n `162`; fx avg `0.0081` n `6`; index avg `0.0109` n `27`; metal avg `0.0124` n `20`; unknown avg `0.1695` n `1276`
- 1h: commodity avg `0.0734` n `13`; crypto_alt avg `0.4664` n `239`; crypto_major avg `0.3316` n `8`; equity avg `0.6801` n `162`; fx avg `0.0167` n `6`; index avg `0.0562` n `27`; metal avg `0.108` n `20`; unknown avg `158.6696` n `1264`
- 4h: commodity avg `0.2849` n `13`; crypto_alt avg `-0.1904` n `239`; crypto_major avg `-0.4391` n `8`; equity avg `-0.1638` n `162`; fx avg `-0.0541` n `6`; index avg `0.0104` n `27`; metal avg `-0.0974` n `20`; unknown avg `-0.043` n `1238`
- 24h: commodity avg `-0.7616` n `13`; crypto_alt avg `0.4003` n `239`; crypto_major avg `0.2666` n `8`; equity avg `-2.5449` n `162`; fx avg `-0.0538` n `6`; index avg `-0.2663` n `27`; metal avg `-0.1745` n `20`; unknown avg `11.3693` n `1115`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
