# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T08:37:41.919637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1556` n `12`; crypto_alt avg `0.1839` n `230`; crypto_major avg `0.2486` n `8`; equity avg `0.2907` n `102`; fx avg `0.0137` n `6`; index avg `0.0393` n `25`; metal avg `0.1141` n `20`; unknown avg `-0.0933` n `779`
- 1h: commodity avg `-0.2578` n `12`; crypto_alt avg `0.195` n `230`; crypto_major avg `0.308` n `8`; equity avg `0.6349` n `102`; fx avg `0.0319` n `6`; index avg `0.1665` n `25`; metal avg `0.2954` n `20`; unknown avg `-0.0719` n `779`
- 4h: commodity avg `0.1015` n `12`; crypto_alt avg `0.2216` n `230`; crypto_major avg `0.3467` n `8`; equity avg `0.3369` n `102`; fx avg `0.0127` n `6`; index avg `-0.0481` n `25`; metal avg `0.2236` n `20`; unknown avg `-0.0871` n `747`
- 24h: commodity avg `0.6792` n `12`; crypto_alt avg `-0.1754` n `230`; crypto_major avg `-0.2309` n `8`; equity avg `-2.6605` n `102`; fx avg `-0.0` n `6`; index avg `-0.3422` n `25`; metal avg `0.2363` n `20`; unknown avg `-0.479` n `745`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
