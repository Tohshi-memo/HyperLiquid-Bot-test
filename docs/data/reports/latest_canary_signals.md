# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T06:52:24.601640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0339` n `13`; crypto_alt avg `-0.0114` n `235`; crypto_major avg `-0.0104` n `8`; equity avg `0.0053` n `150`; fx avg `-0.0128` n `6`; index avg `-0.0114` n `26`; metal avg `-0.0238` n `20`; unknown avg `1.4339` n `1076`
- 1h: commodity avg `0.1029` n `13`; crypto_alt avg `0.0753` n `235`; crypto_major avg `0.1082` n `8`; equity avg `-0.1157` n `150`; fx avg `-0.0031` n `6`; index avg `-0.0435` n `26`; metal avg `-0.1184` n `20`; unknown avg `1.4267` n `1052`
- 4h: commodity avg `0.1497` n `13`; crypto_alt avg `0.0584` n `235`; crypto_major avg `0.4854` n `8`; equity avg `-0.0306` n `150`; fx avg `-0.0268` n `6`; index avg `-0.0545` n `26`; metal avg `-0.1792` n `20`; unknown avg `1.2603` n `1046`
- 24h: commodity avg `0.8961` n `13`; crypto_alt avg `-2.9005` n `235`; crypto_major avg `-1.71` n `8`; equity avg `-0.2346` n `149`; fx avg `0.049` n `6`; index avg `-0.1018` n `26`; metal avg `-0.184` n `20`; unknown avg `871.0631` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
