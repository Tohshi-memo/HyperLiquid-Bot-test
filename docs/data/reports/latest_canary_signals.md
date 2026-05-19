# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T00:37:17.067905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0169` n `12`; crypto_alt avg `-0.0692` n `228`; crypto_major avg `-0.1779` n `8`; equity avg `0.0381` n `66`; fx avg `0.0183` n `6`; index avg `0.0179` n `23`; metal avg `-0.2406` n `18`; unknown avg `0.0013` n `383`
- 1h: commodity avg `0.0924` n `12`; crypto_alt avg `0.4426` n `228`; crypto_major avg `0.3682` n `8`; equity avg `0.0743` n `66`; fx avg `0.0997` n `6`; index avg `0.0294` n `23`; metal avg `-0.2022` n `18`; unknown avg `0.1724` n `383`
- 4h: commodity avg `0.2791` n `12`; crypto_alt avg `1.0866` n `228`; crypto_major avg `0.9` n `8`; equity avg `0.606` n `66`; fx avg `0.0669` n `6`; index avg `0.2716` n `23`; metal avg `0.4133` n `18`; unknown avg `-0.0046` n `383`
- 24h: commodity avg `0.3951` n `12`; crypto_alt avg `1.7471` n `228`; crypto_major avg `0.4907` n `8`; equity avg `0.5659` n `66`; fx avg `0.2372` n `6`; index avg `0.3995` n `23`; metal avg `2.2037` n `18`; unknown avg `0.7329` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
