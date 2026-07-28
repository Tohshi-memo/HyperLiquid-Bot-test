# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T16:37:29.862697+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.29` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.8139` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0308` n `12`; crypto_alt avg `-0.0757` n `230`; crypto_major avg `-0.0637` n `8`; equity avg `-0.0754` n `102`; fx avg `0.0075` n `6`; index avg `0.012` n `25`; metal avg `-0.0189` n `20`; unknown avg `-0.0574` n `774`
- 1h: commodity avg `-0.1871` n `12`; crypto_alt avg `-0.1644` n `230`; crypto_major avg `-0.1942` n `8`; equity avg `-0.113` n `102`; fx avg `-0.0064` n `6`; index avg `0.01` n `25`; metal avg `0.0823` n `20`; unknown avg `-0.2546` n `774`
- 4h: commodity avg `-0.7856` n `12`; crypto_alt avg `0.4957` n `230`; crypto_major avg `1.0816` n `8`; equity avg `-0.7323` n `102`; fx avg `-0.0182` n `6`; index avg `0.097` n `25`; metal avg `0.1884` n `20`; unknown avg `-0.0191` n `774`
- 24h: commodity avg `-1.2153` n `12`; crypto_alt avg `-1.7962` n `230`; crypto_major avg `-1.8162` n `8`; equity avg `-3.0569` n `102`; fx avg `-0.1079` n `6`; index avg `-0.2439` n `25`; metal avg `-0.4087` n `20`; unknown avg `1225.2736` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
