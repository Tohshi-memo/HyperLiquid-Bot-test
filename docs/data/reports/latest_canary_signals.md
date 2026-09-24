# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T15:22:35.023525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.1943` n `234`; crypto_major avg `0.2675` n `8`; equity avg `-0.0522` n `141`; fx avg `0.0089` n `6`; index avg `-0.0071` n `26`; metal avg `0.0587` n `20`; unknown avg `0.8228` n `943`
- 1h: commodity avg `0.5167` n `12`; crypto_alt avg `-0.2632` n `234`; crypto_major avg `-0.0724` n `8`; equity avg `-0.2802` n `141`; fx avg `0.0235` n `6`; index avg `-0.0671` n `26`; metal avg `-0.0706` n `20`; unknown avg `4.7083` n `895`
- 4h: commodity avg `0.6312` n `12`; crypto_alt avg `2.1687` n `234`; crypto_major avg `1.2329` n `8`; equity avg `-0.0682` n `141`; fx avg `-0.0025` n `6`; index avg `-0.0433` n `26`; metal avg `-0.1183` n `20`; unknown avg `4.6661` n `889`
- 24h: commodity avg `1.0944` n `12`; crypto_alt avg `0.803` n `234`; crypto_major avg `-0.4374` n `8`; equity avg `-1.719` n `141`; fx avg `0.0413` n `6`; index avg `-0.3116` n `26`; metal avg `-0.3019` n `20`; unknown avg `265.5966` n `823`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
