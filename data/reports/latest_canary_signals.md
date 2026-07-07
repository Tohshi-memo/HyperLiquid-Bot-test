# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T16:37:28.273132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6178` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.021` n `12`; crypto_alt avg `-0.0013` n `229`; crypto_major avg `-0.0842` n `8`; equity avg `-0.101` n `91`; fx avg `-0.0016` n `6`; index avg `0.0036` n `25`; metal avg `-0.0164` n `20`; unknown avg `-0.0348` n `763`
- 1h: commodity avg `0.0547` n `12`; crypto_alt avg `0.0649` n `229`; crypto_major avg `-0.1235` n `8`; equity avg `0.7827` n `91`; fx avg `-0.0325` n `6`; index avg `0.184` n `25`; metal avg `0.0647` n `20`; unknown avg `0.188` n `763`
- 4h: commodity avg `0.564` n `12`; crypto_alt avg `-0.0121` n `229`; crypto_major avg `0.4344` n `8`; equity avg `-1.1834` n `91`; fx avg `-0.0286` n `6`; index avg `-0.1297` n `25`; metal avg `-0.1997` n `20`; unknown avg `-0.0463` n `755`
- 24h: commodity avg `0.6129` n `12`; crypto_alt avg `-0.7762` n `229`; crypto_major avg `-0.256` n `8`; equity avg `-3.2638` n `91`; fx avg `-0.2436` n `6`; index avg `-0.5757` n `25`; metal avg `0.0363` n `20`; unknown avg `-0.0134` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
