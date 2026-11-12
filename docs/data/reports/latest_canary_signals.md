# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T20:22:27.719103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0654` n `13`; crypto_alt avg `0.0713` n `239`; crypto_major avg `0.1008` n `8`; equity avg `0.0404` n `162`; fx avg `-0.0038` n `6`; index avg `0.0142` n `27`; metal avg `0.0246` n `20`; unknown avg `0.2696` n `1257`
- 1h: commodity avg `0.0862` n `13`; crypto_alt avg `-0.0254` n `239`; crypto_major avg `0.1749` n `8`; equity avg `-0.1922` n `162`; fx avg `-0.0083` n `6`; index avg `-0.0043` n `27`; metal avg `0.0234` n `20`; unknown avg `161.7552` n `1241`
- 4h: commodity avg `0.6215` n `13`; crypto_alt avg `-0.1361` n `239`; crypto_major avg `-0.1049` n `8`; equity avg `-1.2087` n `162`; fx avg `-0.028` n `6`; index avg `-0.1085` n `27`; metal avg `0.006` n `20`; unknown avg `69.6343` n `1229`
- 24h: commodity avg `0.905` n `13`; crypto_alt avg `-2.5508` n `239`; crypto_major avg `-2.9363` n `8`; equity avg `-2.6564` n `162`; fx avg `-0.1478` n `6`; index avg `-0.1553` n `27`; metal avg `-0.7022` n `20`; unknown avg `30.7734` n `1137`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
