# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T01:57:50.922497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0614` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0055` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0486` n `12`; crypto_alt avg `-0.5628` n `234`; crypto_major avg `-0.504` n `8`; equity avg `-0.3065` n `141`; fx avg `0.002` n `6`; index avg `-0.0452` n `26`; metal avg `0.0211` n `20`; unknown avg `-0.3254` n `956`
- 1h: commodity avg `0.0093` n `12`; crypto_alt avg `-1.348` n `234`; crypto_major avg `-1.1106` n `8`; equity avg `-0.8002` n `141`; fx avg `0.0481` n `6`; index avg `-0.1051` n `26`; metal avg `-0.2062` n `20`; unknown avg `2.1855` n `950`
- 4h: commodity avg `-0.4435` n `12`; crypto_alt avg `-1.131` n `234`; crypto_major avg `-1.2069` n `8`; equity avg `-1.3116` n `141`; fx avg `0.1293` n `6`; index avg `-0.1455` n `26`; metal avg `-0.5573` n `20`; unknown avg `2.4311` n `910`
- 24h: commodity avg `-0.4597` n `12`; crypto_alt avg `-0.3899` n `234`; crypto_major avg `-1.1422` n `8`; equity avg `-1.0457` n `141`; fx avg `0.0925` n `6`; index avg `-0.0946` n `26`; metal avg `-0.5803` n `20`; unknown avg `13.4914` n `819`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
