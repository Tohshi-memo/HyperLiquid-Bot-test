# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T18:37:33.653054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.3343` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.9881` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5742` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0323` n `12`; crypto_alt avg `-0.1813` n `231`; crypto_major avg `-0.3161` n `8`; equity avg `-0.0944` n `122`; fx avg `0.0055` n `6`; index avg `0.0043` n `25`; metal avg `-0.0566` n `20`; unknown avg `0.0128` n `794`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `0.4818` n `231`; crypto_major avg `0.2482` n `8`; equity avg `0.3242` n `122`; fx avg `0.0023` n `6`; index avg `0.0932` n `25`; metal avg `-0.0803` n `20`; unknown avg `-0.1349` n `794`
- 4h: commodity avg `-0.1152` n `12`; crypto_alt avg `-1.2267` n `231`; crypto_major avg `-1.8893` n `8`; equity avg `0.445` n `122`; fx avg `-0.0328` n `6`; index avg `0.0988` n `25`; metal avg `-0.3151` n `20`; unknown avg `0.1787` n `793`
- 24h: commodity avg `-0.1943` n `12`; crypto_alt avg `-1.5459` n `231`; crypto_major avg `-0.9191` n `8`; equity avg `-2.3289` n `122`; fx avg `-0.142` n `6`; index avg `-0.2766` n `25`; metal avg `-0.0075` n `20`; unknown avg `2.7069` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
