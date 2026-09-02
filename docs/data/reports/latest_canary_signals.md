# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T21:37:29.745606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `-0.0721` n `232`; crypto_major avg `0.0184` n `8`; equity avg `0.0683` n `133`; fx avg `0.0042` n `6`; index avg `0.0132` n `26`; metal avg `-0.009` n `20`; unknown avg `-0.0649` n `792`
- 1h: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.1951` n `232`; crypto_major avg `-0.1025` n `8`; equity avg `0.2124` n `133`; fx avg `-0.0078` n `6`; index avg `0.0282` n `26`; metal avg `-0.0119` n `20`; unknown avg `-0.0331` n `784`
- 4h: commodity avg `0.0441` n `12`; crypto_alt avg `0.1903` n `232`; crypto_major avg `0.4477` n `8`; equity avg `0.7563` n `133`; fx avg `-0.0311` n `6`; index avg `0.0423` n `26`; metal avg `0.1137` n `20`; unknown avg `-0.2254` n `772`
- 24h: commodity avg `0.2216` n `12`; crypto_alt avg `0.0701` n `232`; crypto_major avg `0.1738` n `8`; equity avg `1.005` n `133`; fx avg `-0.3909` n `6`; index avg `0.117` n `26`; metal avg `0.4462` n `20`; unknown avg `0.3063` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0456`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0445`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0441`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
