# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T01:07:23.793129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2137` n `12`; crypto_alt avg `-0.2423` n `228`; crypto_major avg `-0.1735` n `8`; equity avg `-0.2834` n `66`; fx avg `0.0353` n `6`; index avg `-0.1422` n `23`; metal avg `-0.1214` n `18`; unknown avg `-0.0663` n `383`
- 1h: commodity avg `0.064` n `12`; crypto_alt avg `0.1577` n `228`; crypto_major avg `0.1445` n `8`; equity avg `-0.2035` n `66`; fx avg `0.0566` n `6`; index avg `-0.1458` n `23`; metal avg `-0.463` n `18`; unknown avg `-0.0736` n `383`
- 4h: commodity avg `0.0876` n `12`; crypto_alt avg `1.2589` n `228`; crypto_major avg `0.9818` n `8`; equity avg `0.2203` n `66`; fx avg `0.1055` n `6`; index avg `-0.0014` n `23`; metal avg `-0.0021` n `18`; unknown avg `-0.1081` n `383`
- 24h: commodity avg `0.1516` n `12`; crypto_alt avg `1.2257` n `228`; crypto_major avg `0.3112` n `8`; equity avg `-0.0981` n `66`; fx avg `0.2416` n `6`; index avg `0.0245` n `23`; metal avg `2.2118` n `18`; unknown avg `0.3161` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
