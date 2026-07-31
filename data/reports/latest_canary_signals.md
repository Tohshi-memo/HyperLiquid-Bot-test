# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T03:22:30.369545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0575` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `0.2709` n `230`; crypto_major avg `0.2154` n `8`; equity avg `0.2124` n `102`; fx avg `0.0232` n `6`; index avg `0.0467` n `25`; metal avg `-0.0183` n `20`; unknown avg `6.6876` n `779`
- 1h: commodity avg `0.0194` n `12`; crypto_alt avg `-0.013` n `230`; crypto_major avg `0.0014` n `8`; equity avg `0.2811` n `102`; fx avg `0.0746` n `6`; index avg `0.0628` n `25`; metal avg `-0.0733` n `20`; unknown avg `-0.0397` n `779`
- 4h: commodity avg `-0.2467` n `12`; crypto_alt avg `-0.303` n `230`; crypto_major avg `-0.7568` n `8`; equity avg `0.6642` n `102`; fx avg `0.2344` n `6`; index avg `0.3007` n `25`; metal avg `-0.2969` n `20`; unknown avg `0.2297` n `779`
- 24h: commodity avg `-0.1145` n `12`; crypto_alt avg `-0.0419` n `230`; crypto_major avg `0.6514` n `8`; equity avg `8.3169` n `102`; fx avg `-0.127` n `6`; index avg `1.1593` n `25`; metal avg `0.4435` n `20`; unknown avg `0.1035` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
