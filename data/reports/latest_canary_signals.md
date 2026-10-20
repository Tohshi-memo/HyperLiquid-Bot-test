# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T14:42:49.385341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.5163` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.7338` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4229` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.923` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1743` n `13`; crypto_alt avg `0.8206` n `237`; crypto_major avg `0.4974` n `8`; equity avg `0.6604` n `151`; fx avg `-0.0125` n `6`; index avg `0.0897` n `26`; metal avg `0.1128` n `20`; unknown avg `-0.5998` n `1199`
- 1h: commodity avg `-0.521` n `13`; crypto_alt avg `2.9025` n `237`; crypto_major avg `2.2128` n `8`; equity avg `2.1255` n `151`; fx avg `0.0315` n `6`; index avg `0.2963` n `26`; metal avg `0.2898` n `20`; unknown avg `1.4451` n `1108`
- 4h: commodity avg `-0.7734` n `13`; crypto_alt avg `3.6045` n `237`; crypto_major avg `2.7429` n `8`; equity avg `2.2467` n `151`; fx avg `0.0637` n `6`; index avg `0.354` n `26`; metal avg `0.32` n `20`; unknown avg `3.441` n `1100`
- 24h: commodity avg `-0.3835` n `13`; crypto_alt avg `4.1488` n `237`; crypto_major avg `2.673` n `8`; equity avg `0.3868` n `151`; fx avg `0.04` n `6`; index avg `0.0698` n `26`; metal avg `0.233` n `20`; unknown avg `4.5815` n `1043`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
