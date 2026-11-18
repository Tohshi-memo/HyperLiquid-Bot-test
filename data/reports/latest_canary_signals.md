# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T05:52:27.636126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.018` n `13`; crypto_alt avg `0.1004` n `239`; crypto_major avg `-0.0809` n `8`; equity avg `0.1254` n `163`; fx avg `0.0108` n `6`; index avg `0.0214` n `27`; metal avg `-0.0029` n `20`; unknown avg `37.6992` n `1258`
- 1h: commodity avg `0.0285` n `13`; crypto_alt avg `0.557` n `239`; crypto_major avg `0.4354` n `8`; equity avg `0.4452` n `163`; fx avg `0.0153` n `6`; index avg `0.0383` n `27`; metal avg `0.0753` n `20`; unknown avg `12.8597` n `1254`
- 4h: commodity avg `-0.1566` n `13`; crypto_alt avg `0.2484` n `239`; crypto_major avg `0.4571` n `8`; equity avg `0.3552` n `163`; fx avg `-0.0012` n `6`; index avg `0.087` n `27`; metal avg `-0.2693` n `20`; unknown avg `14.019` n `1244`
- 24h: commodity avg `0.2006` n `13`; crypto_alt avg `0.0341` n `239`; crypto_major avg `0.3812` n `8`; equity avg `0.4448` n `163`; fx avg `-0.0854` n `6`; index avg `0.0363` n `27`; metal avg `-0.8481` n `20`; unknown avg `496.3887` n `1065`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
