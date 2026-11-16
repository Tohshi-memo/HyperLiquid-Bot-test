# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T10:07:52.213859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.019` n `13`; crypto_alt avg `0.1459` n `239`; crypto_major avg `0.1486` n `8`; equity avg `-0.0367` n `162`; fx avg `0.0201` n `6`; index avg `-0.0097` n `27`; metal avg `0.0288` n `20`; unknown avg `0.0788` n `1259`
- 1h: commodity avg `0.0809` n `13`; crypto_alt avg `0.2453` n `239`; crypto_major avg `0.2207` n `8`; equity avg `-0.2484` n `162`; fx avg `-0.0234` n `6`; index avg `-0.0356` n `27`; metal avg `-0.1036` n `20`; unknown avg `0.0628` n `1261`
- 4h: commodity avg `-0.1169` n `13`; crypto_alt avg `-0.2275` n `239`; crypto_major avg `-0.1382` n `8`; equity avg `-0.1311` n `162`; fx avg `-0.0223` n `6`; index avg `0.0146` n `27`; metal avg `-0.0458` n `20`; unknown avg `34.18` n `1093`
- 24h: commodity avg `-0.3451` n `13`; crypto_alt avg `-1.2842` n `239`; crypto_major avg `-1.4258` n `8`; equity avg `-1.035` n `162`; fx avg `-0.0701` n `6`; index avg `-0.0657` n `27`; metal avg `-0.0839` n `20`; unknown avg `34.6739` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
