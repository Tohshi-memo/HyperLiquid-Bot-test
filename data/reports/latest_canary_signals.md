# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T21:22:28.295415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1248` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0243` n `12`; crypto_alt avg `-0.1876` n `233`; crypto_major avg `-0.147` n `8`; equity avg `-0.0023` n `136`; fx avg `0.0119` n `6`; index avg `-0.0119` n `27`; metal avg `0.0199` n `20`; unknown avg `0.3638` n `908`
- 1h: commodity avg `0.0262` n `12`; crypto_alt avg `-0.7539` n `233`; crypto_major avg `-1.1047` n `8`; equity avg `0.0419` n `136`; fx avg `0.0075` n `6`; index avg `0.0201` n `27`; metal avg `0.0485` n `20`; unknown avg `10.4649` n `886`
- 4h: commodity avg `-0.0572` n `12`; crypto_alt avg `0.157` n `233`; crypto_major avg `0.617` n `8`; equity avg `-0.4087` n `136`; fx avg `0.004` n `6`; index avg `-0.0735` n `27`; metal avg `-0.0786` n `20`; unknown avg `4.075` n `874`
- 24h: commodity avg `0.2462` n `12`; crypto_alt avg `0.1323` n `233`; crypto_major avg `2.0965` n `8`; equity avg `-0.6702` n `136`; fx avg `0.0406` n `6`; index avg `-0.22` n `27`; metal avg `-0.3779` n `20`; unknown avg `4.8144` n `684`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
