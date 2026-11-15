# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T08:37:27.391842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0758` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.02` n `13`; crypto_alt avg `0.0085` n `239`; crypto_major avg `0.2554` n `8`; equity avg `0.023` n `162`; fx avg `-0.0013` n `6`; index avg `0.0011` n `27`; metal avg `0.0138` n `20`; unknown avg `0.0893` n `1263`
- 1h: commodity avg `0.003` n `13`; crypto_alt avg `-0.3594` n `239`; crypto_major avg `0.3736` n `8`; equity avg `0.0379` n `162`; fx avg `-0.009` n `6`; index avg `0.0038` n `27`; metal avg `0.0139` n `20`; unknown avg `0.4302` n `1245`
- 4h: commodity avg `-0.0224` n `13`; crypto_alt avg `-1.0687` n `239`; crypto_major avg `-1.1014` n `8`; equity avg `-0.2212` n `162`; fx avg `-0.0118` n `6`; index avg `-0.0256` n `27`; metal avg `0.0782` n `20`; unknown avg `0.2587` n `1223`
- 24h: commodity avg `0.0174` n `13`; crypto_alt avg `-5.4918` n `239`; crypto_major avg `-4.5791` n `8`; equity avg `-1.0669` n `162`; fx avg `-0.1381` n `6`; index avg `-0.1005` n `27`; metal avg `-0.4092` n `20`; unknown avg `46.6514` n `1059`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
