# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T12:07:26.614841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3623` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `0.2405` n `230`; crypto_major avg `0.5177` n `8`; equity avg `0.0281` n `121`; fx avg `0.0023` n `6`; index avg `0.0029` n `25`; metal avg `0.0083` n `20`; unknown avg `0.0638` n `794`
- 1h: commodity avg `-0.0037` n `12`; crypto_alt avg `0.5352` n `230`; crypto_major avg `0.6593` n `8`; equity avg `0.0863` n `121`; fx avg `0.0067` n `6`; index avg `0.0094` n `25`; metal avg `0.0357` n `20`; unknown avg `0.1534` n `794`
- 4h: commodity avg `-0.0277` n `12`; crypto_alt avg `-1.6331` n `230`; crypto_major avg `-1.359` n `8`; equity avg `-0.0996` n `121`; fx avg `0.0366` n `6`; index avg `0.0033` n `25`; metal avg `0.0294` n `20`; unknown avg `0.0655` n `794`
- 24h: commodity avg `0.0085` n `12`; crypto_alt avg `2.047` n `230`; crypto_major avg `4.217` n `8`; equity avg `-0.8961` n `121`; fx avg `0.0544` n `6`; index avg `-0.1213` n `25`; metal avg `-0.1728` n `20`; unknown avg `1.4782` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
