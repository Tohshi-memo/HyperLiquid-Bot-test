# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T08:52:28.884515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.57` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0441` n `13`; crypto_alt avg `-0.0539` n `238`; crypto_major avg `-0.141` n `8`; equity avg `-0.0457` n `154`; fx avg `-0.0043` n `6`; index avg `-0.0024` n `27`; metal avg `0.0234` n `20`; unknown avg `1.2226` n `1238`
- 1h: commodity avg `-0.1962` n `13`; crypto_alt avg `0.2933` n `238`; crypto_major avg `0.493` n `8`; equity avg `0.0732` n `154`; fx avg `0.0199` n `6`; index avg `0.0078` n `27`; metal avg `0.079` n `20`; unknown avg `77.0684` n `1208`
- 4h: commodity avg `-0.0496` n `13`; crypto_alt avg `0.1529` n `238`; crypto_major avg `0.4836` n `8`; equity avg `0.2594` n `154`; fx avg `-0.0481` n `6`; index avg `0.0595` n `27`; metal avg `0.0703` n `20`; unknown avg `14.033` n `1194`
- 24h: commodity avg `-0.3387` n `13`; crypto_alt avg `2.1429` n `238`; crypto_major avg `2.6918` n `8`; equity avg `3.849` n `154`; fx avg `0.0729` n `6`; index avg `0.4968` n `27`; metal avg `0.4845` n `20`; unknown avg `16.1613` n `1026`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
