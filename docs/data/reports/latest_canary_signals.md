# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T07:22:23.991430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8353` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7667` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5018` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.3997` n `230`; crypto_major avg `-0.4788` n `8`; equity avg `-0.0549` n `121`; fx avg `0.0076` n `6`; index avg `-0.0109` n `25`; metal avg `0.0` n `20`; unknown avg `0.0084` n `794`
- 1h: commodity avg `-0.0213` n `12`; crypto_alt avg `0.6871` n `230`; crypto_major avg `0.7327` n `8`; equity avg `0.0779` n `121`; fx avg `-0.008` n `6`; index avg `0.0081` n `25`; metal avg `0.0075` n `20`; unknown avg `0.6913` n `794`
- 4h: commodity avg `0.068` n `12`; crypto_alt avg `-3.1946` n `230`; crypto_major avg `-1.8855` n `8`; equity avg `-0.3837` n `121`; fx avg `0.0057` n `6`; index avg `-0.0502` n `25`; metal avg `-0.1188` n `20`; unknown avg `0.518` n `777`
- 24h: commodity avg `0.1556` n `12`; crypto_alt avg `6.1475` n `230`; crypto_major avg `6.5889` n `8`; equity avg `-0.5625` n `121`; fx avg `0.026` n `6`; index avg `-0.0996` n `25`; metal avg `-0.0327` n `20`; unknown avg `1.8497` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
