# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T05:07:27.533233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0569` n `12`; crypto_alt avg `0.1723` n `232`; crypto_major avg `0.2204` n `8`; equity avg `0.2624` n `128`; fx avg `0.0137` n `6`; index avg `0.0526` n `26`; metal avg `0.0173` n `20`; unknown avg `0.1325` n `791`
- 1h: commodity avg `0.0746` n `12`; crypto_alt avg `-0.0535` n `232`; crypto_major avg `0.0458` n `8`; equity avg `0.4594` n `128`; fx avg `0.0265` n `6`; index avg `0.1167` n `26`; metal avg `0.0845` n `20`; unknown avg `-0.1678` n `791`
- 4h: commodity avg `0.1541` n `12`; crypto_alt avg `0.7119` n `231`; crypto_major avg `0.1193` n `8`; equity avg `0.5258` n `128`; fx avg `-0.042` n `6`; index avg `0.2028` n `26`; metal avg `-0.1068` n `20`; unknown avg `-0.4716` n `779`
- 24h: commodity avg `0.4385` n `12`; crypto_alt avg `-0.427` n `231`; crypto_major avg `-2.0633` n `8`; equity avg `-0.7477` n `128`; fx avg `-0.0309` n `6`; index avg `-0.1161` n `26`; metal avg `-0.3434` n `20`; unknown avg `-0.5206` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
