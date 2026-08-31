# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T01:22:26.360005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5257` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5042` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `0.2429` n `231`; crypto_major avg `0.1166` n `8`; equity avg `-0.0746` n `128`; fx avg `-0.0213` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0619` n `20`; unknown avg `-0.0103` n `793`
- 1h: commodity avg `0.1645` n `12`; crypto_alt avg `0.0313` n `231`; crypto_major avg `-0.3941` n `8`; equity avg `-0.3466` n `128`; fx avg `-0.0361` n `6`; index avg `-0.0547` n `26`; metal avg `-0.2096` n `20`; unknown avg `-0.0957` n `791`
- 4h: commodity avg `-0.212` n `12`; crypto_alt avg `-1.5686` n `231`; crypto_major avg `-1.8293` n `8`; equity avg `-1.263` n `128`; fx avg `-0.0163` n `6`; index avg `-0.3036` n `26`; metal avg `-0.3251` n `20`; unknown avg `2.5138` n `791`
- 24h: commodity avg `0.2934` n `12`; crypto_alt avg `-0.5946` n `231`; crypto_major avg `-2.0096` n `8`; equity avg `-1.3022` n `128`; fx avg `-0.0055` n `6`; index avg `-0.3106` n `26`; metal avg `-0.2989` n `20`; unknown avg `-0.4392` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
