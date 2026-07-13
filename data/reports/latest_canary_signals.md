# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T04:37:26.140792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5589` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3403` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0116` n `12`; crypto_alt avg `-0.193` n `230`; crypto_major avg `-0.3257` n `8`; equity avg `-0.1099` n `92`; fx avg `0.004` n `6`; index avg `-0.0327` n `25`; metal avg `-0.0166` n `20`; unknown avg `0.1715` n `766`
- 1h: commodity avg `0.0109` n `12`; crypto_alt avg `0.2728` n `230`; crypto_major avg `-0.0236` n `8`; equity avg `-0.1594` n `92`; fx avg `-0.0018` n `6`; index avg `-0.078` n `25`; metal avg `0.0202` n `20`; unknown avg `0.0623` n `766`
- 4h: commodity avg `0.031` n `12`; crypto_alt avg `-1.6183` n `230`; crypto_major avg `-1.7728` n `8`; equity avg `-1.944` n `92`; fx avg `0.0406` n `6`; index avg `-0.4325` n `25`; metal avg `-0.2139` n `20`; unknown avg `3.8091` n `766`
- 24h: commodity avg `0.1294` n `12`; crypto_alt avg `-2.1006` n `230`; crypto_major avg `-1.3156` n `8`; equity avg `-2.4804` n `92`; fx avg `0.0421` n `6`; index avg `-0.5402` n `25`; metal avg `-0.5041` n `20`; unknown avg `-0.1` n `741`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
