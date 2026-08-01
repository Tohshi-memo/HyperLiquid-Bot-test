# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T19:22:27.996543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2079` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0386` n `12`; crypto_alt avg `-0.15` n `230`; crypto_major avg `-0.101` n `8`; equity avg `0.0434` n `102`; fx avg `-0.0041` n `6`; index avg `0.0142` n `25`; metal avg `0.0179` n `20`; unknown avg `-0.0507` n `782`
- 1h: commodity avg `0.0825` n `12`; crypto_alt avg `-0.5436` n `230`; crypto_major avg `-0.5027` n `8`; equity avg `-0.0554` n `102`; fx avg `0.0116` n `6`; index avg `-0.0018` n `25`; metal avg `0.0486` n `20`; unknown avg `0.8704` n `782`
- 4h: commodity avg `0.1133` n `12`; crypto_alt avg `-1.1208` n `230`; crypto_major avg `-1.2377` n `8`; equity avg `-0.2992` n `102`; fx avg `-0.016` n `6`; index avg `-0.0298` n `25`; metal avg `0.0075` n `20`; unknown avg `2.3125` n `782`
- 24h: commodity avg `0.5695` n `12`; crypto_alt avg `-0.9719` n `230`; crypto_major avg `-1.5073` n `8`; equity avg `-1.3415` n `102`; fx avg `-0.1702` n `6`; index avg `-0.1762` n `25`; metal avg `-0.0701` n `20`; unknown avg `4.1676` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
