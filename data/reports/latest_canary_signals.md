# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T23:22:26.848992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0598` n `13`; crypto_alt avg `-0.1186` n `239`; crypto_major avg `-0.2595` n `8`; equity avg `-0.0343` n `162`; fx avg `-0.0003` n `6`; index avg `-0.0057` n `27`; metal avg `-0.0243` n `20`; unknown avg `0.3811` n `1263`
- 1h: commodity avg `-0.2295` n `13`; crypto_alt avg `0.1572` n `239`; crypto_major avg `0.0825` n `8`; equity avg `0.6106` n `162`; fx avg `-0.0054` n `6`; index avg `0.1372` n `27`; metal avg `0.271` n `20`; unknown avg `0.1871` n `1229`
- 4h: commodity avg `-0.3047` n `13`; crypto_alt avg `0.4062` n `239`; crypto_major avg `0.5718` n `8`; equity avg `0.8092` n `162`; fx avg `0.0197` n `6`; index avg `0.1403` n `27`; metal avg `0.3267` n `20`; unknown avg `0.5968` n `1185`
- 24h: commodity avg `-0.3109` n `13`; crypto_alt avg `3.3837` n `239`; crypto_major avg `4.1458` n `8`; equity avg `1.9929` n `162`; fx avg `0.008` n `6`; index avg `0.2394` n `27`; metal avg `0.4629` n `20`; unknown avg `2.9978` n `1138`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
