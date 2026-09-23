# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T12:37:31.987986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1027` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0163` n `12`; crypto_alt avg `0.1669` n `234`; crypto_major avg `0.0669` n `8`; equity avg `0.135` n `140`; fx avg `0.0189` n `6`; index avg `0.0195` n `26`; metal avg `-0.0865` n `20`; unknown avg `353.4976` n `946`
- 1h: commodity avg `0.0241` n `12`; crypto_alt avg `0.6043` n `234`; crypto_major avg `0.1488` n `8`; equity avg `0.1481` n `140`; fx avg `0.0204` n `6`; index avg `0.0131` n `26`; metal avg `0.006` n `20`; unknown avg `399.7741` n `938`
- 4h: commodity avg `0.1401` n `12`; crypto_alt avg `-0.9082` n `234`; crypto_major avg `-1.1745` n `8`; equity avg `-0.5078` n `140`; fx avg `-0.0126` n `6`; index avg `-0.0718` n `26`; metal avg `-0.2179` n `20`; unknown avg `3.5345` n `937`
- 24h: commodity avg `0.7707` n `12`; crypto_alt avg `2.8146` n `234`; crypto_major avg `-0.1234` n `8`; equity avg `0.567` n `140`; fx avg `0.0014` n `6`; index avg `0.0083` n `26`; metal avg `-0.4159` n `20`; unknown avg `3.0613` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
