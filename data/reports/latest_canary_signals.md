# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T12:23:10.839272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2233` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0376` n `12`; crypto_alt avg `0.0786` n `234`; crypto_major avg `-0.012` n `8`; equity avg `-0.015` n `140`; fx avg `-0.0025` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0352` n `20`; unknown avg `1.1329` n `946`
- 1h: commodity avg `0.1389` n `12`; crypto_alt avg `0.1192` n `234`; crypto_major avg `-0.1435` n `8`; equity avg `-0.1965` n `140`; fx avg `-0.0169` n `6`; index avg `-0.0409` n `26`; metal avg `0.0058` n `20`; unknown avg `20.3034` n `938`
- 4h: commodity avg `0.241` n `12`; crypto_alt avg `-0.9997` n `234`; crypto_major avg `-1.3231` n `8`; equity avg `-0.6769` n `140`; fx avg `-0.0162` n `6`; index avg `-0.0998` n `26`; metal avg `-0.1617` n `20`; unknown avg `4.5997` n `937`
- 24h: commodity avg `0.7123` n `12`; crypto_alt avg `2.9249` n `234`; crypto_major avg `-0.0331` n `8`; equity avg `0.4184` n `140`; fx avg `-0.0159` n `6`; index avg `0.0032` n `26`; metal avg `-0.3139` n `20`; unknown avg `2.8392` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
