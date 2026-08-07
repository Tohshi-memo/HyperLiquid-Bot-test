# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T18:52:32.137097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `12`; crypto_alt avg `-0.1487` n `230`; crypto_major avg `-0.1539` n `8`; equity avg `-0.0356` n `112`; fx avg `0.0028` n `6`; index avg `0.0066` n `25`; metal avg `-0.0085` n `20`; unknown avg `0.0846` n `782`
- 1h: commodity avg `0.0094` n `12`; crypto_alt avg `-0.0657` n `230`; crypto_major avg `-0.0412` n `8`; equity avg `-0.0916` n `112`; fx avg `0.0064` n `6`; index avg `-0.0239` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.0431` n `782`
- 4h: commodity avg `0.0766` n `12`; crypto_alt avg `-0.1323` n `230`; crypto_major avg `-0.8201` n `8`; equity avg `0.4267` n `112`; fx avg `-0.0171` n `6`; index avg `0.0184` n `25`; metal avg `-0.0204` n `20`; unknown avg `0.0478` n `782`
- 24h: commodity avg `0.3661` n `12`; crypto_alt avg `-0.6848` n `230`; crypto_major avg `-0.9088` n `8`; equity avg `0.4608` n `112`; fx avg `-0.1341` n `6`; index avg `-0.0694` n `25`; metal avg `0.2919` n `20`; unknown avg `-0.1396` n `765`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.3071`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2873`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2387`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
