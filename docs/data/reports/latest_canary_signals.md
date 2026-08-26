# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T16:37:32.377040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2291` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `-0.2268` n `231`; crypto_major avg `-0.192` n `8`; equity avg `-0.0853` n `122`; fx avg `-0.0054` n `6`; index avg `-0.0086` n `25`; metal avg `-0.0162` n `20`; unknown avg `-0.0956` n `797`
- 1h: commodity avg `0.2765` n `12`; crypto_alt avg `-0.4985` n `231`; crypto_major avg `-0.3145` n `8`; equity avg `-0.2082` n `122`; fx avg `0.0092` n `6`; index avg `-0.0334` n `25`; metal avg `-0.1238` n `20`; unknown avg `-0.063` n `797`
- 4h: commodity avg `0.649` n `12`; crypto_alt avg `-1.7837` n `231`; crypto_major avg `-1.2304` n `8`; equity avg `-0.1051` n `122`; fx avg `0.0051` n `6`; index avg `-0.0013` n `25`; metal avg `-0.2821` n `20`; unknown avg `-0.2408` n `797`
- 24h: commodity avg `0.4086` n `12`; crypto_alt avg `-2.7315` n `231`; crypto_major avg `-2.4857` n `8`; equity avg `-0.6201` n `122`; fx avg `-0.0428` n `6`; index avg `-0.0244` n `25`; metal avg `-0.3183` n `20`; unknown avg `0.2867` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
