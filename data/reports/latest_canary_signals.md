# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T01:00:59.517259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2152` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1418` n `12`; crypto_alt avg `0.0017` n `231`; crypto_major avg `-0.0792` n `8`; equity avg `-0.3461` n `128`; fx avg `-0.0067` n `6`; index avg `-0.0783` n `26`; metal avg `-0.1968` n `20`; unknown avg `-0.0608` n `791`
- 1h: commodity avg `0.0949` n `12`; crypto_alt avg `0.8506` n `231`; crypto_major avg `0.5183` n `8`; equity avg `0.2253` n `128`; fx avg `-0.0075` n `6`; index avg `0.0615` n `26`; metal avg `-0.1229` n `20`; unknown avg `0.4098` n `791`
- 4h: commodity avg `-0.2095` n `12`; crypto_alt avg `-1.2316` n `231`; crypto_major avg `-1.5099` n `8`; equity avg `-1.1734` n `128`; fx avg `0.0044` n `6`; index avg `-0.2947` n `26`; metal avg `-0.2801` n `20`; unknown avg `3.2794` n `791`
- 24h: commodity avg `0.2698` n `12`; crypto_alt avg `-0.5365` n `231`; crypto_major avg `-1.7173` n `8`; equity avg `-1.195` n `128`; fx avg `0.0217` n `6`; index avg `-0.3064` n `26`; metal avg `-0.2494` n `20`; unknown avg `-0.3696` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0476`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0433`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
