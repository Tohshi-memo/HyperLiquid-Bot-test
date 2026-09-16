# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T19:52:26.520348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.58` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.87` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `0.4784` n `234`; crypto_major avg `0.5248` n `8`; equity avg `0.4106` n `137`; fx avg `-0.0034` n `6`; index avg `0.0814` n `27`; metal avg `0.0468` n `20`; unknown avg `1.7883` n `917`
- 1h: commodity avg `-0.0455` n `12`; crypto_alt avg `0.1788` n `234`; crypto_major avg `0.4301` n `8`; equity avg `-0.2241` n `137`; fx avg `0.0539` n `6`; index avg `-0.0824` n `27`; metal avg `-0.1231` n `20`; unknown avg `14.8754` n `879`
- 4h: commodity avg `-0.0651` n `12`; crypto_alt avg `0.9156` n `234`; crypto_major avg `0.8614` n `8`; equity avg `-1.0086` n `137`; fx avg `0.041` n `6`; index avg `-0.268` n `27`; metal avg `-0.6133` n `20`; unknown avg `0.3143` n `869`
- 24h: commodity avg `-0.6909` n `12`; crypto_alt avg `-0.8163` n `234`; crypto_major avg `0.398` n `8`; equity avg `0.5909` n `137`; fx avg `0.064` n `6`; index avg `0.0229` n `27`; metal avg `-0.2998` n `20`; unknown avg `0.6244` n `799`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
