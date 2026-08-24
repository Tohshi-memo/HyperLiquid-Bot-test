# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T17:37:28.670654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.5834` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.5431` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.249` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.035` n `12`; crypto_alt avg `-0.2689` n `231`; crypto_major avg `-0.1532` n `8`; equity avg `-0.1312` n `122`; fx avg `-0.0037` n `6`; index avg `-0.033` n `25`; metal avg `-0.0074` n `20`; unknown avg `-0.0642` n `794`
- 1h: commodity avg `-0.0385` n `12`; crypto_alt avg `-1.6053` n `231`; crypto_major avg `-1.6519` n `8`; equity avg `-0.408` n `122`; fx avg `0.0001` n `6`; index avg `-0.0685` n `25`; metal avg `-0.1088` n `20`; unknown avg `0.1562` n `793`
- 4h: commodity avg `-0.2967` n `12`; crypto_alt avg `-0.9089` n `231`; crypto_major avg `-1.2723` n `8`; equity avg `0.2053` n `122`; fx avg `-0.0325` n `6`; index avg `-0.0233` n `25`; metal avg `-0.2252` n `20`; unknown avg `-0.1025` n `793`
- 24h: commodity avg `-0.2309` n `12`; crypto_alt avg `-1.7681` n `231`; crypto_major avg `-0.8973` n `8`; equity avg `-2.5487` n `122`; fx avg `-0.154` n `6`; index avg `-0.3308` n `25`; metal avg `0.0958` n `20`; unknown avg `3.3826` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
