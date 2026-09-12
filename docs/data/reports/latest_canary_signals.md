# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T18:52:29.556751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `12`; crypto_alt avg `-0.0313` n `233`; crypto_major avg `-0.0142` n `8`; equity avg `-0.0066` n `136`; fx avg `0.0006` n `6`; index avg `-0.0027` n `26`; metal avg `0.0019` n `20`; unknown avg `0.5293` n `830`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `-0.1096` n `233`; crypto_major avg `-0.2115` n `8`; equity avg `-0.0204` n `136`; fx avg `-0.0012` n `6`; index avg `-0.0056` n `26`; metal avg `0.01` n `20`; unknown avg `0.1808` n `796`
- 4h: commodity avg `0.0684` n `12`; crypto_alt avg `-0.078` n `233`; crypto_major avg `-0.4502` n `8`; equity avg `-0.0234` n `136`; fx avg `-0.0049` n `6`; index avg `-0.0038` n `26`; metal avg `0.0126` n `20`; unknown avg `0.3237` n `782`
- 24h: commodity avg `-0.2141` n `12`; crypto_alt avg `1.7326` n `233`; crypto_major avg `0.4067` n `8`; equity avg `-0.0183` n `136`; fx avg `-0.0255` n `6`; index avg `0.0152` n `26`; metal avg `0.0417` n `20`; unknown avg `1.3091` n `692`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0467`, n `668`, weak_sample_signal
