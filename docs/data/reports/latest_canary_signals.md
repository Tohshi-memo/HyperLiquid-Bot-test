# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T18:07:38.094346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1067` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0807` n `13`; crypto_alt avg `0.4197` n `239`; crypto_major avg `0.4131` n `8`; equity avg `0.3439` n `156`; fx avg `-0.009` n `6`; index avg `0.0508` n `27`; metal avg `0.0801` n `20`; unknown avg `0.2797` n `1241`
- 1h: commodity avg `-0.2435` n `13`; crypto_alt avg `-0.7148` n `239`; crypto_major avg `-0.5591` n `8`; equity avg `-0.5713` n `156`; fx avg `-0.0184` n `6`; index avg `-0.0461` n `27`; metal avg `-0.0581` n `20`; unknown avg `0.4448` n `1235`
- 4h: commodity avg `-0.6293` n `13`; crypto_alt avg `-1.3928` n `239`; crypto_major avg `-1.185` n `8`; equity avg `-1.8993` n `156`; fx avg `0.0107` n `6`; index avg `-0.0783` n `27`; metal avg `0.1229` n `20`; unknown avg `178.2985` n `1229`
- 24h: commodity avg `-1.4357` n `13`; crypto_alt avg `-2.8237` n `238`; crypto_major avg `-1.4117` n `8`; equity avg `-1.3654` n `156`; fx avg `0.2675` n `6`; index avg `0.1706` n `27`; metal avg `0.3574` n `20`; unknown avg `160.52` n `1055`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
