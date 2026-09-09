# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T23:07:30.160583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7324` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7283` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `0.3967` n `233`; crypto_major avg `0.2191` n `8`; equity avg `0.0229` n `134`; fx avg `-0.003` n `6`; index avg `0.0016` n `26`; metal avg `0.0237` n `20`; unknown avg `0.0826` n `795`
- 1h: commodity avg `-0.0346` n `12`; crypto_alt avg `-0.4838` n `233`; crypto_major avg `-0.1278` n `8`; equity avg `-0.0455` n `134`; fx avg `-0.0111` n `6`; index avg `0.0003` n `26`; metal avg `0.0114` n `20`; unknown avg `0.3168` n `763`
- 4h: commodity avg `0.0946` n `12`; crypto_alt avg `-2.7671` n `233`; crypto_major avg `-1.725` n `8`; equity avg `-0.3962` n `134`; fx avg `-0.0181` n `6`; index avg `0.0033` n `26`; metal avg `0.0074` n `20`; unknown avg `20.9841` n `691`
- 24h: commodity avg `0.1439` n `12`; crypto_alt avg `-3.2311` n `233`; crypto_major avg `-2.1293` n `8`; equity avg `-0.6671` n `134`; fx avg `-0.0213` n `6`; index avg `-0.1348` n `26`; metal avg `0.5778` n `20`; unknown avg `0.9776` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
