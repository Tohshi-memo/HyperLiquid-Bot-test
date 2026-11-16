# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T12:22:25.305142+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0424` n `13`; crypto_alt avg `-0.3793` n `239`; crypto_major avg `-0.2959` n `8`; equity avg `-0.3067` n `162`; fx avg `0.0118` n `6`; index avg `-0.055` n `27`; metal avg `-0.0158` n `20`; unknown avg `0.1817` n `1263`
- 1h: commodity avg `-0.1398` n `13`; crypto_alt avg `-0.9495` n `239`; crypto_major avg `-1.1152` n `8`; equity avg `-0.9159` n `162`; fx avg `0.0044` n `6`; index avg `-0.1367` n `27`; metal avg `0.0017` n `20`; unknown avg `0.2591` n `1253`
- 4h: commodity avg `-0.2933` n `13`; crypto_alt avg `-0.3432` n `239`; crypto_major avg `-0.4285` n `8`; equity avg `-1.1879` n `162`; fx avg `-0.0231` n `6`; index avg `-0.1624` n `27`; metal avg `0.0695` n `20`; unknown avg `16.9743` n `1253`
- 24h: commodity avg `-0.4947` n `13`; crypto_alt avg `-2.004` n `239`; crypto_major avg `-1.9051` n `8`; equity avg `-1.6724` n `162`; fx avg `-0.0485` n `6`; index avg `-0.1715` n `27`; metal avg `0.0309` n `20`; unknown avg `23.413` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
