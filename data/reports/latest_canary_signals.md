# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T21:07:37.136509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `13`; crypto_alt avg `0.0676` n `235`; crypto_major avg `0.0124` n `8`; equity avg `-0.0142` n `150`; fx avg `0.0126` n `6`; index avg `0.0026` n `26`; metal avg `0.0228` n `20`; unknown avg `0.0227` n `1067`
- 1h: commodity avg `0.0932` n `13`; crypto_alt avg `0.2474` n `235`; crypto_major avg `0.0832` n `8`; equity avg `0.0391` n `150`; fx avg `0.0176` n `6`; index avg `0.0008` n `26`; metal avg `0.0402` n `20`; unknown avg `-0.1588` n `1025`
- 4h: commodity avg `0.1685` n `13`; crypto_alt avg `0.459` n `235`; crypto_major avg `-0.189` n `8`; equity avg `0.0362` n `150`; fx avg `0.046` n `6`; index avg `-0.002` n `26`; metal avg `-0.112` n `20`; unknown avg `0.5616` n `999`
- 24h: commodity avg `0.3929` n `13`; crypto_alt avg `-4.0571` n `235`; crypto_major avg `-3.4096` n `8`; equity avg `-1.4452` n `150`; fx avg `-0.1422` n `6`; index avg `-0.2269` n `26`; metal avg `-0.6849` n `20`; unknown avg `1.0659` n `972`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
