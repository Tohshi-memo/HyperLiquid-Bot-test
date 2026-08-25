# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T07:37:29.483549+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `-0.0039` n `231`; crypto_major avg `-0.1054` n `8`; equity avg `-0.0783` n `122`; fx avg `0.01` n `6`; index avg `0.0001` n `25`; metal avg `-0.0656` n `20`; unknown avg `0.0968` n `794`
- 1h: commodity avg `-0.0096` n `12`; crypto_alt avg `-0.0063` n `231`; crypto_major avg `0.0985` n `8`; equity avg `-0.1102` n `122`; fx avg `0.0161` n `6`; index avg `-0.0351` n `25`; metal avg `-0.0898` n `20`; unknown avg `0.0139` n `794`
- 4h: commodity avg `-0.2555` n `12`; crypto_alt avg `-0.4301` n `231`; crypto_major avg `-0.4563` n `8`; equity avg `0.5421` n `122`; fx avg `0.0502` n `6`; index avg `0.0983` n `25`; metal avg `-0.0196` n `20`; unknown avg `-0.1657` n `778`
- 24h: commodity avg `-0.2227` n `12`; crypto_alt avg `1.6635` n `231`; crypto_major avg `2.499` n `8`; equity avg `0.1067` n `122`; fx avg `0.0206` n `6`; index avg `0.0095` n `25`; metal avg `-0.2293` n `20`; unknown avg `0.5432` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
