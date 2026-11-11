# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T09:52:31.145456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0298` n `13`; crypto_alt avg `0.2515` n `239`; crypto_major avg `0.2283` n `8`; equity avg `0.1253` n `161`; fx avg `0.0045` n `6`; index avg `0.009` n `27`; metal avg `0.0752` n `20`; unknown avg `13.2263` n `1261`
- 1h: commodity avg `0.1723` n `13`; crypto_alt avg `-0.183` n `239`; crypto_major avg `0.0311` n `8`; equity avg `0.0439` n `161`; fx avg `-0.0388` n `6`; index avg `-0.0136` n `27`; metal avg `0.0988` n `20`; unknown avg `-0.217` n `1239`
- 4h: commodity avg `0.1749` n `13`; crypto_alt avg `-0.5984` n `239`; crypto_major avg `-0.2774` n `8`; equity avg `0.2931` n `161`; fx avg `-0.0858` n `6`; index avg `-0.0274` n `27`; metal avg `0.0877` n `20`; unknown avg `-0.032` n `1201`
- 24h: commodity avg `0.949` n `13`; crypto_alt avg `-1.285` n `239`; crypto_major avg `-1.9986` n `8`; equity avg `1.6676` n `161`; fx avg `-0.2489` n `6`; index avg `0.1823` n `27`; metal avg `0.2402` n `20`; unknown avg `1.0358` n `1175`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
