# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T14:24:29.714282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.2495` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0276` n `12`; crypto_alt avg `-0.3488` n `230`; crypto_major avg `-0.3204` n `8`; equity avg `-1.1882` n `93`; fx avg `0.0108` n `6`; index avg `-0.1863` n `25`; metal avg `-0.0931` n `20`; unknown avg `0.024` n `768`
- 1h: commodity avg `-0.0734` n `12`; crypto_alt avg `-0.7468` n `230`; crypto_major avg `-0.6726` n `8`; equity avg `-1.4949` n `93`; fx avg `0.0392` n `6`; index avg `-0.2838` n `25`; metal avg `-0.0681` n `20`; unknown avg `0.1363` n `768`
- 4h: commodity avg `-0.1778` n `12`; crypto_alt avg `0.5138` n `230`; crypto_major avg `0.8069` n `8`; equity avg `-1.4426` n `93`; fx avg `0.0674` n `6`; index avg `-0.285` n `25`; metal avg `0.177` n `20`; unknown avg `0.0756` n `767`
- 24h: commodity avg `0.0341` n `12`; crypto_alt avg `0.7481` n `230`; crypto_major avg `1.8741` n `8`; equity avg `-0.2646` n `92`; fx avg `0.0886` n `6`; index avg `-0.0772` n `25`; metal avg `-0.163` n `20`; unknown avg `0.1815` n `738`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
