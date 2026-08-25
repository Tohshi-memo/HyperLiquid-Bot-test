# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T00:52:27.899426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.8038` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6589` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0359` n `12`; crypto_alt avg `0.7022` n `231`; crypto_major avg `0.6995` n `8`; equity avg `0.1332` n `122`; fx avg `0.0067` n `6`; index avg `0.0252` n `25`; metal avg `-0.0266` n `20`; unknown avg `1.939` n `794`
- 1h: commodity avg `-0.0631` n `12`; crypto_alt avg `1.0464` n `231`; crypto_major avg `1.3119` n `8`; equity avg `0.1565` n `122`; fx avg `0.0251` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0097` n `20`; unknown avg `1.6572` n `794`
- 4h: commodity avg `-0.0237` n `12`; crypto_alt avg `1.0575` n `231`; crypto_major avg `1.8679` n `8`; equity avg `0.0641` n `122`; fx avg `0.0193` n `6`; index avg `-0.0241` n `25`; metal avg `0.209` n `20`; unknown avg `-0.0098` n `794`
- 24h: commodity avg `-0.0681` n `12`; crypto_alt avg `0.396` n `231`; crypto_major avg `1.1598` n `8`; equity avg `-2.4759` n `122`; fx avg `0.0175` n `6`; index avg `-0.3493` n `25`; metal avg `0.3168` n `20`; unknown avg `0.8831` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
