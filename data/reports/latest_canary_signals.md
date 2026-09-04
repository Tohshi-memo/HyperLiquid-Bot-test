# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T00:37:23.500439+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `12`; crypto_alt avg `0.1613` n `232`; crypto_major avg `0.2289` n `8`; equity avg `0.0512` n `133`; fx avg `0.017` n `6`; index avg `0.009` n `26`; metal avg `0.0069` n `20`; unknown avg `18.41` n `786`
- 1h: commodity avg `-0.0465` n `12`; crypto_alt avg `0.2151` n `232`; crypto_major avg `0.1795` n `8`; equity avg `0.2619` n `133`; fx avg `0.0201` n `6`; index avg `0.0149` n `26`; metal avg `-0.0083` n `20`; unknown avg `17.0827` n `784`
- 4h: commodity avg `-0.0083` n `12`; crypto_alt avg `0.0839` n `232`; crypto_major avg `0.027` n `8`; equity avg `0.2203` n `133`; fx avg `0.0296` n `6`; index avg `0.0086` n `26`; metal avg `0.0037` n `20`; unknown avg `1.2911` n `778`
- 24h: commodity avg `-0.1523` n `12`; crypto_alt avg `4.394` n `232`; crypto_major avg `5.6133` n `8`; equity avg `1.5742` n `133`; fx avg `-0.2344` n `6`; index avg `0.22` n `26`; metal avg `0.8107` n `20`; unknown avg `23.1025` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
