# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T06:22:23.545797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `0.0273` n `231`; crypto_major avg `-0.1832` n `8`; equity avg `0.0905` n `127`; fx avg `0.0084` n `6`; index avg `0.0174` n `26`; metal avg `0.0485` n `20`; unknown avg `0.0618` n `791`
- 1h: commodity avg `-0.0541` n `12`; crypto_alt avg `0.1931` n `231`; crypto_major avg `0.1405` n `8`; equity avg `0.0069` n `127`; fx avg `0.0102` n `6`; index avg `-0.0034` n `26`; metal avg `-0.1067` n `20`; unknown avg `0.0747` n `775`
- 4h: commodity avg `-0.0295` n `12`; crypto_alt avg `-0.5295` n `231`; crypto_major avg `-0.242` n `8`; equity avg `-0.1093` n `127`; fx avg `0.0272` n `6`; index avg `-0.0793` n `26`; metal avg `-0.2259` n `20`; unknown avg `0.0563` n `775`
- 24h: commodity avg `0.2841` n `12`; crypto_alt avg `-0.0723` n `231`; crypto_major avg `0.4076` n `8`; equity avg `1.2619` n `127`; fx avg `-0.0833` n `6`; index avg `0.2044` n `26`; metal avg `-0.2931` n `20`; unknown avg `0.3754` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
