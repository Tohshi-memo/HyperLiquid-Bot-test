# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T04:37:38.724039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `0.0495` n `230`; crypto_major avg `0.0148` n `8`; equity avg `-0.0801` n `108`; fx avg `0.0044` n `6`; index avg `-0.0121` n `25`; metal avg `-0.0125` n `20`; unknown avg `0.0608` n `782`
- 1h: commodity avg `-0.0652` n `12`; crypto_alt avg `0.2782` n `230`; crypto_major avg `0.3034` n `8`; equity avg `0.0305` n `108`; fx avg `0.0035` n `6`; index avg `0.0164` n `25`; metal avg `-0.0235` n `20`; unknown avg `0.1195` n `782`
- 4h: commodity avg `-0.0463` n `12`; crypto_alt avg `-0.1255` n `230`; crypto_major avg `-0.429` n `8`; equity avg `0.1614` n `108`; fx avg `-0.0278` n `6`; index avg `-0.0524` n `25`; metal avg `-0.1261` n `20`; unknown avg `-0.104` n `782`
- 24h: commodity avg `-0.1018` n `12`; crypto_alt avg `0.1355` n `230`; crypto_major avg `0.1201` n `8`; equity avg `-1.8734` n `108`; fx avg `-0.0065` n `6`; index avg `-0.3477` n `25`; metal avg `0.4827` n `20`; unknown avg `0.9423` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1822`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
