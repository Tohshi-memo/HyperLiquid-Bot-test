# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T01:52:25.291579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1323` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0072` n `13`; crypto_alt avg `-0.1888` n `239`; crypto_major avg `-0.0806` n `8`; equity avg `0.2064` n `161`; fx avg `-0.0007` n `6`; index avg `0.0266` n `27`; metal avg `-0.0634` n `20`; unknown avg `22.7994` n `1262`
- 1h: commodity avg `-0.0759` n `13`; crypto_alt avg `-0.6261` n `239`; crypto_major avg `-0.622` n `8`; equity avg `0.481` n `161`; fx avg `0.0098` n `6`; index avg `0.0283` n `27`; metal avg `-0.0079` n `20`; unknown avg `23.0644` n `1256`
- 4h: commodity avg `-0.1331` n `13`; crypto_alt avg `-1.3558` n `239`; crypto_major avg `-1.2273` n `8`; equity avg `-1.1461` n `161`; fx avg `0.0067` n `6`; index avg `-0.095` n `27`; metal avg `-0.022` n `20`; unknown avg `7.2695` n `1242`
- 24h: commodity avg `0.1127` n `13`; crypto_alt avg `-1.8439` n `239`; crypto_major avg `-0.5873` n `8`; equity avg `1.6011` n `161`; fx avg `-0.1401` n `6`; index avg `0.1496` n `27`; metal avg `-0.3444` n `20`; unknown avg `5.0048` n `1141`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
