# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T19:52:46.779273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.36` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.1094` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `-0.1511` n `230`; crypto_major avg `-0.1049` n `8`; equity avg `0.074` n `94`; fx avg `0.0015` n `6`; index avg `0.0191` n `25`; metal avg `0.0229` n `20`; unknown avg `-0.0881` n `768`
- 1h: commodity avg `0.1419` n `12`; crypto_alt avg `-0.3239` n `230`; crypto_major avg `-0.3763` n `8`; equity avg `0.244` n `94`; fx avg `0.0032` n `6`; index avg `0.0519` n `25`; metal avg `-0.0409` n `20`; unknown avg `-0.0682` n `768`
- 4h: commodity avg `0.3836` n `12`; crypto_alt avg `-0.722` n `230`; crypto_major avg `-1.0088` n `8`; equity avg `0.3701` n `94`; fx avg `0.0709` n `6`; index avg `0.1006` n `25`; metal avg `0.2506` n `20`; unknown avg `0.1083` n `768`
- 24h: commodity avg `0.1774` n `12`; crypto_alt avg `0.1629` n `230`; crypto_major avg `0.4412` n `8`; equity avg `-0.4475` n `93`; fx avg `0.2111` n `6`; index avg `-0.1686` n `25`; metal avg `0.1365` n `20`; unknown avg `0.1686` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
