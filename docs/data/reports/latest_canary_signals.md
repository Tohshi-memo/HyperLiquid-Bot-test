# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T05:07:26.820269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `13`; crypto_alt avg `-0.1029` n `239`; crypto_major avg `-0.0022` n `8`; equity avg `-0.237` n `162`; fx avg `-0.0037` n `6`; index avg `-0.0368` n `27`; metal avg `-0.0177` n `20`; unknown avg `4.5808` n `1260`
- 1h: commodity avg `0.0` n `13`; crypto_alt avg `0.0093` n `239`; crypto_major avg `0.0842` n `8`; equity avg `-0.1435` n `162`; fx avg `-0.0233` n `6`; index avg `-0.002` n `27`; metal avg `0.0508` n `20`; unknown avg `0.5574` n `1254`
- 4h: commodity avg `-0.2099` n `13`; crypto_alt avg `0.9765` n `239`; crypto_major avg `0.9217` n `8`; equity avg `0.1622` n `162`; fx avg `-0.0228` n `6`; index avg `-0.0521` n `27`; metal avg `0.2184` n `20`; unknown avg `8.7212` n `1242`
- 24h: commodity avg `-1.1635` n `13`; crypto_alt avg `0.7417` n `239`; crypto_major avg `1.4706` n `8`; equity avg `-2.3682` n `162`; fx avg `-0.0469` n `6`; index avg `-0.2459` n `27`; metal avg `-0.0145` n `20`; unknown avg `562.7737` n `985`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
