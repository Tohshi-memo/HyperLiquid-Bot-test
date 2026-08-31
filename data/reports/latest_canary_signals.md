# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T12:37:25.880345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `-0.4115` n `232`; crypto_major avg `-0.3027` n `8`; equity avg `-0.1487` n `128`; fx avg `0.0046` n `6`; index avg `-0.0172` n `26`; metal avg `-0.0181` n `20`; unknown avg `-0.0333` n `794`
- 1h: commodity avg `-0.2289` n `12`; crypto_alt avg `-0.3393` n `232`; crypto_major avg `-0.2584` n `8`; equity avg `-0.0754` n `128`; fx avg `0.0236` n `6`; index avg `-0.0035` n `26`; metal avg `-0.1011` n `20`; unknown avg `0.1187` n `792`
- 4h: commodity avg `0.0362` n `12`; crypto_alt avg `-0.1972` n `232`; crypto_major avg `0.2041` n `8`; equity avg `-0.288` n `128`; fx avg `0.0208` n `6`; index avg `-0.0544` n `26`; metal avg `0.004` n `20`; unknown avg `0.2093` n `791`
- 24h: commodity avg `0.5542` n `12`; crypto_alt avg `-1.0934` n `231`; crypto_major avg `-1.4536` n `8`; equity avg `-0.5346` n `128`; fx avg `-0.114` n `6`; index avg `-0.1123` n `26`; metal avg `-0.2157` n `20`; unknown avg `0.0137` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
