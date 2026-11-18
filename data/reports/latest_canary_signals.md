# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T12:22:27.018493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0157` n `13`; crypto_alt avg `0.1087` n `239`; crypto_major avg `0.2684` n `8`; equity avg `0.133` n `163`; fx avg `-0.0019` n `6`; index avg `0.0195` n `27`; metal avg `0.0013` n `20`; unknown avg `0.4692` n `1264`
- 1h: commodity avg `0.0905` n `13`; crypto_alt avg `0.1145` n `239`; crypto_major avg `0.2369` n `8`; equity avg `0.0201` n `163`; fx avg `-0.0137` n `6`; index avg `-0.0101` n `27`; metal avg `0.0935` n `20`; unknown avg `2.5333` n `1258`
- 4h: commodity avg `0.2262` n `13`; crypto_alt avg `0.1449` n `239`; crypto_major avg `-0.3249` n `8`; equity avg `-0.0885` n `163`; fx avg `0.0253` n `6`; index avg `-0.0033` n `27`; metal avg `0.0887` n `20`; unknown avg `113.7632` n `1200`
- 24h: commodity avg `-0.0702` n `13`; crypto_alt avg `-0.025` n `239`; crypto_major avg `0.2406` n `8`; equity avg `-0.1809` n `163`; fx avg `-0.1191` n `6`; index avg `-0.0098` n `27`; metal avg `-1.0729` n `20`; unknown avg `5.8317` n `1099`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
