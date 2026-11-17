# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T08:37:28.666999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `13`; crypto_alt avg `-0.2031` n `239`; crypto_major avg `-0.3412` n `8`; equity avg `-0.1071` n `162`; fx avg `-0.0106` n `6`; index avg `-0.027` n `27`; metal avg `-0.0095` n `20`; unknown avg `7.1787` n `1266`
- 1h: commodity avg `0.0235` n `13`; crypto_alt avg `-0.3634` n `239`; crypto_major avg `-0.4367` n `8`; equity avg `-0.0672` n `162`; fx avg `-0.0151` n `6`; index avg `-0.005` n `27`; metal avg `-0.0897` n `20`; unknown avg `0.1816` n `1238`
- 4h: commodity avg `0.1569` n `13`; crypto_alt avg `-0.4337` n `239`; crypto_major avg `-0.6732` n `8`; equity avg `-0.5361` n `162`; fx avg `-0.0089` n `6`; index avg `-0.0385` n `27`; metal avg `-0.0769` n `20`; unknown avg `-0.1167` n `1172`
- 24h: commodity avg `-0.9915` n `13`; crypto_alt avg `0.7847` n `239`; crypto_major avg `0.8785` n `8`; equity avg `-2.6845` n `162`; fx avg `-0.0246` n `6`; index avg `-0.2979` n `27`; metal avg `-0.0622` n `20`; unknown avg `37.2966` n `1115`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
