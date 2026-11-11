# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T23:07:28.843337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.092` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.0353` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0135` n `13`; crypto_alt avg `-0.2061` n `239`; crypto_major avg `-0.2344` n `8`; equity avg `-0.3429` n `161`; fx avg `-0.0012` n `6`; index avg `0.0093` n `27`; metal avg `-0.0337` n `20`; unknown avg `4.9371` n `1258`
- 1h: commodity avg `-0.0438` n `13`; crypto_alt avg `-1.2481` n `239`; crypto_major avg `-1.1844` n `8`; equity avg `-1.3859` n `161`; fx avg `-0.0173` n `6`; index avg `-0.0924` n `27`; metal avg `-0.0491` n `20`; unknown avg `44.1885` n `1256`
- 4h: commodity avg `-0.1766` n `13`; crypto_alt avg `-1.3784` n `239`; crypto_major avg `-1.1992` n `8`; equity avg `-1.9315` n `161`; fx avg `-0.0215` n `6`; index avg `-0.1639` n `27`; metal avg `-0.0952` n `20`; unknown avg `25.8877` n `1204`
- 24h: commodity avg `0.1957` n `13`; crypto_alt avg `-0.8979` n `239`; crypto_major avg `0.0094` n `8`; equity avg `2.9952` n `161`; fx avg `-0.1726` n `6`; index avg `0.3512` n `27`; metal avg `-0.1199` n `20`; unknown avg `3.9634` n `1141`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
