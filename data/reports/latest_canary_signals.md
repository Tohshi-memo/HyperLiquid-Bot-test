# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T16:07:29.854866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1215` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.3773` n `12`; crypto_alt avg `0.8008` n `234`; crypto_major avg `0.7685` n `8`; equity avg `0.7298` n `141`; fx avg `-0.0286` n `6`; index avg `0.1811` n `26`; metal avg `0.201` n `20`; unknown avg `1.8704` n `940`
- 1h: commodity avg `-0.306` n `12`; crypto_alt avg `-0.064` n `234`; crypto_major avg `-0.1335` n `8`; equity avg `0.3755` n `141`; fx avg `-0.0339` n `6`; index avg `0.0998` n `26`; metal avg `0.1489` n `20`; unknown avg `1.1128` n `930`
- 4h: commodity avg `-0.198` n `12`; crypto_alt avg `-0.6277` n `234`; crypto_major avg `-1.0935` n `8`; equity avg `-0.5339` n `141`; fx avg `-0.0563` n `6`; index avg `0.028` n `26`; metal avg `0.0009` n `20`; unknown avg `12.4842` n `894`
- 24h: commodity avg `-1.1457` n `12`; crypto_alt avg `2.0431` n `234`; crypto_major avg `1.2056` n `8`; equity avg `1.2506` n `141`; fx avg `-0.2868` n `6`; index avg `0.3684` n `26`; metal avg `0.3983` n `20`; unknown avg `1609.6072` n `805`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
