# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T16:56:43.096188+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3405` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0524` n `12`; crypto_alt avg `0.092` n `231`; crypto_major avg `0.0197` n `8`; equity avg `0.0355` n `122`; fx avg `0.0015` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0263` n `20`; unknown avg `0.0971` n `797`
- 1h: commodity avg `0.0185` n `12`; crypto_alt avg `-0.3608` n `231`; crypto_major avg `-0.2709` n `8`; equity avg `-0.0514` n `122`; fx avg `0.0042` n `6`; index avg `-0.0398` n `25`; metal avg `-0.041` n `20`; unknown avg `-0.067` n `797`
- 4h: commodity avg `0.5967` n `12`; crypto_alt avg `-1.6235` n `231`; crypto_major avg `-1.3286` n `8`; equity avg `0.0369` n `122`; fx avg `-0.0037` n `6`; index avg `0.0119` n `25`; metal avg `-0.2977` n `20`; unknown avg `-0.3048` n `797`
- 24h: commodity avg `0.3673` n `12`; crypto_alt avg `-2.7543` n `231`; crypto_major avg `-2.5561` n `8`; equity avg `-0.5014` n `122`; fx avg `-0.0317` n `6`; index avg `-0.013` n `25`; metal avg `-0.3617` n `20`; unknown avg `0.2367` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
