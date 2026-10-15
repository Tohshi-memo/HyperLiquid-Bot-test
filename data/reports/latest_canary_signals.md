# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T15:21:18.300099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5711` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0379` n `13`; crypto_alt avg `0.0836` n `236`; crypto_major avg `0.107` n `8`; equity avg `0.4531` n `151`; fx avg `0.0057` n `6`; index avg `0.0301` n `26`; metal avg `0.056` n `20`; unknown avg `0.1379` n `1136`
- 1h: commodity avg `0.1009` n `13`; crypto_alt avg `2.1591` n `236`; crypto_major avg `1.5321` n `8`; equity avg `1.7656` n `151`; fx avg `-0.0235` n `6`; index avg `0.1859` n `26`; metal avg `0.1102` n `20`; unknown avg `1.3031` n `1130`
- 4h: commodity avg `0.1781` n `13`; crypto_alt avg `2.7516` n `236`; crypto_major avg `1.6348` n `8`; equity avg `1.6417` n `151`; fx avg `-0.0077` n `6`; index avg `0.2733` n `26`; metal avg `0.0637` n `20`; unknown avg `4.1032` n `1082`
- 24h: commodity avg `0.069` n `13`; crypto_alt avg `-0.1575` n `236`; crypto_major avg `-0.3829` n `8`; equity avg `-2.4222` n `151`; fx avg `0.1934` n `6`; index avg `-0.4001` n `26`; metal avg `0.3181` n `20`; unknown avg `-0.5932` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.11`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1004`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0821`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0795`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0726`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0662`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0616`, n `666`, weak_sample_signal
