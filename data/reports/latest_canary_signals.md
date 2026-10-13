# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T20:22:30.389162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0492` n `13`; crypto_alt avg `-0.2432` n `235`; crypto_major avg `-0.2028` n `8`; equity avg `-0.0823` n `151`; fx avg `0.0148` n `6`; index avg `-0.016` n `26`; metal avg `-0.032` n `20`; unknown avg `0.2224` n `1097`
- 1h: commodity avg `0.1491` n `13`; crypto_alt avg `-0.1393` n `235`; crypto_major avg `-0.2478` n `8`; equity avg `0.202` n `151`; fx avg `-0.0047` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0358` n `20`; unknown avg `0.389` n `1081`
- 4h: commodity avg `0.3541` n `13`; crypto_alt avg `0.0837` n `235`; crypto_major avg `-0.3077` n `8`; equity avg `0.2724` n `151`; fx avg `0.014` n `6`; index avg `0.0395` n `26`; metal avg `-0.0167` n `20`; unknown avg `0.0483` n `1081`
- 24h: commodity avg `0.9736` n `13`; crypto_alt avg `-1.5531` n `235`; crypto_major avg `-0.799` n `8`; equity avg `-0.7142` n `151`; fx avg `0.178` n `6`; index avg `-0.1596` n `26`; metal avg `-0.2765` n `20`; unknown avg `0.1509` n `1002`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1577`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1421`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1174`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0921`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0813`, n `666`, weak_sample_signal
