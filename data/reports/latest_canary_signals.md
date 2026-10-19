# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T22:52:24.146076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.02` n `13`; crypto_alt avg `-0.1122` n `237`; crypto_major avg `0.0244` n `8`; equity avg `-0.0402` n `151`; fx avg `-0.0043` n `6`; index avg `-0.0063` n `26`; metal avg `-0.011` n `20`; unknown avg `0.1464` n `1196`
- 1h: commodity avg `0.0047` n `13`; crypto_alt avg `0.5747` n `237`; crypto_major avg `0.3089` n `8`; equity avg `0.0905` n `151`; fx avg `-0.0184` n `6`; index avg `0.0155` n `26`; metal avg `-0.0388` n `20`; unknown avg `0.8317` n `1184`
- 4h: commodity avg `-0.0258` n `13`; crypto_alt avg `0.665` n `237`; crypto_major avg `0.5137` n `8`; equity avg `0.1725` n `151`; fx avg `-0.009` n `6`; index avg `0.0307` n `26`; metal avg `-0.1137` n `20`; unknown avg `2.4359` n `1114`
- 24h: commodity avg `0.0292` n `13`; crypto_alt avg `1.268` n `237`; crypto_major avg `0.7071` n `8`; equity avg `1.511` n `151`; fx avg `-0.0273` n `6`; index avg `0.2968` n `26`; metal avg `-0.1687` n `20`; unknown avg `3.5152` n `980`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
