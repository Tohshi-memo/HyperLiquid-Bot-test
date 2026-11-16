# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T07:37:28.286449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0651` n `13`; crypto_alt avg `0.502` n `239`; crypto_major avg `0.6084` n `8`; equity avg `0.1725` n `162`; fx avg `-0.0053` n `6`; index avg `0.0195` n `27`; metal avg `0.045` n `20`; unknown avg `0.2346` n `1263`
- 1h: commodity avg `-0.1587` n `13`; crypto_alt avg `0.3252` n `239`; crypto_major avg `0.5159` n `8`; equity avg `0.2043` n `162`; fx avg `-0.0197` n `6`; index avg `0.0331` n `27`; metal avg `0.1032` n `20`; unknown avg `88.1929` n `1139`
- 4h: commodity avg `0.1546` n `13`; crypto_alt avg `-0.1717` n `239`; crypto_major avg `0.1305` n `8`; equity avg `-0.6276` n `162`; fx avg `-0.0464` n `6`; index avg `-0.0376` n `27`; metal avg `0.0214` n `20`; unknown avg `89.7444` n `1115`
- 24h: commodity avg `-0.289` n `13`; crypto_alt avg `0.4485` n `239`; crypto_major avg `1.5808` n `8`; equity avg `-0.1857` n `162`; fx avg `-0.064` n `6`; index avg `-0.0024` n `27`; metal avg `0.1311` n `20`; unknown avg `47.2365` n `1077`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
