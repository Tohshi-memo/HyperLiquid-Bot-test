# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T00:22:26.068003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0394` n `13`; crypto_alt avg `-0.1607` n `235`; crypto_major avg `-0.0003` n `8`; equity avg `0.135` n `150`; fx avg `0.0194` n `6`; index avg `0.0278` n `26`; metal avg `0.0952` n `20`; unknown avg `0.1285` n `1134`
- 1h: commodity avg `-0.298` n `13`; crypto_alt avg `0.1065` n `235`; crypto_major avg `0.1123` n `8`; equity avg `0.211` n `150`; fx avg `-0.0085` n `6`; index avg `0.0145` n `26`; metal avg `0.1171` n `20`; unknown avg `-0.0618` n `1126`
- 4h: commodity avg `-0.4048` n `13`; crypto_alt avg `0.1519` n `235`; crypto_major avg `0.1053` n `8`; equity avg `0.3045` n `150`; fx avg `-0.0321` n `6`; index avg `0.0398` n `26`; metal avg `0.1095` n `20`; unknown avg `-0.2551` n `1098`
- 24h: commodity avg `-0.2947` n `13`; crypto_alt avg `2.1702` n `235`; crypto_major avg `0.8817` n `8`; equity avg `0.5858` n `150`; fx avg `-0.0085` n `6`; index avg `0.0695` n `26`; metal avg `0.1874` n `20`; unknown avg `0.5231` n `957`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
