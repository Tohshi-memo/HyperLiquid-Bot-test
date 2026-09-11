# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T19:52:48.837171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.24` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2597` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `0.0894` n `233`; crypto_major avg `0.0766` n `8`; equity avg `-0.0343` n `136`; fx avg `0.0031` n `6`; index avg `-0.0123` n `26`; metal avg `-0.0183` n `20`; unknown avg `-0.1614` n `824`
- 1h: commodity avg `-0.0055` n `12`; crypto_alt avg `0.5043` n `233`; crypto_major avg `0.4976` n `8`; equity avg `-0.0211` n `136`; fx avg `0.0142` n `6`; index avg `-0.0038` n `26`; metal avg `0.0024` n `20`; unknown avg `14.3605` n `804`
- 4h: commodity avg `0.1236` n `12`; crypto_alt avg `-1.4952` n `233`; crypto_major avg `-1.3065` n `8`; equity avg `-0.4305` n `136`; fx avg `0.0177` n `6`; index avg `-0.0468` n `26`; metal avg `-0.1134` n `20`; unknown avg `8.1115` n `752`
- 24h: commodity avg `-0.4609` n `12`; crypto_alt avg `0.4359` n `233`; crypto_major avg `1.1758` n `8`; equity avg `0.653` n `136`; fx avg `-0.144` n `6`; index avg `0.3226` n `26`; metal avg `0.2549` n `20`; unknown avg `4.9855` n `666`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
