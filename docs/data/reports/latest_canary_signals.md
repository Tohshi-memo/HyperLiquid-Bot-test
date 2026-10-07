# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T00:23:06.819785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0317` n `13`; crypto_alt avg `-0.0937` n `235`; crypto_major avg `-0.0252` n `8`; equity avg `0.1466` n `150`; fx avg `0.0201` n `6`; index avg `0.0336` n `26`; metal avg `0.0114` n `20`; unknown avg `0.0452` n `1076`
- 1h: commodity avg `0.0875` n `13`; crypto_alt avg `-0.2584` n `235`; crypto_major avg `-0.0703` n `8`; equity avg `0.126` n `150`; fx avg `0.0389` n `6`; index avg `0.0219` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.2133` n `1068`
- 4h: commodity avg `0.1512` n `13`; crypto_alt avg `-0.4103` n `235`; crypto_major avg `-0.2563` n `8`; equity avg `0.2366` n `150`; fx avg `0.0372` n `6`; index avg `0.0456` n `26`; metal avg `0.0028` n `20`; unknown avg `-0.0176` n `1044`
- 24h: commodity avg `0.4496` n `13`; crypto_alt avg `-1.4844` n `235`; crypto_major avg `-1.1151` n `8`; equity avg `0.4846` n `149`; fx avg `0.1422` n `6`; index avg `0.0214` n `26`; metal avg `0.0308` n `20`; unknown avg `871.2674` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
