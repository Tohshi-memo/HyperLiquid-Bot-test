# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T10:07:23.873545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2598` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.699` n `230`; crypto_major avg `-0.5827` n `8`; equity avg `-0.0393` n `121`; fx avg `0.0035` n `6`; index avg `0.0031` n `25`; metal avg `0.0075` n `20`; unknown avg `0.1374` n `794`
- 1h: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.4534` n `230`; crypto_major avg `-0.5638` n `8`; equity avg `-0.0421` n `121`; fx avg `0.0044` n `6`; index avg `0.0027` n `25`; metal avg `0.0152` n `20`; unknown avg `0.3094` n `794`
- 4h: commodity avg `-0.0317` n `12`; crypto_alt avg `-1.1413` n `230`; crypto_major avg `-1.2712` n `8`; equity avg `-0.0858` n `121`; fx avg `-0.0062` n `6`; index avg `-0.0114` n `25`; metal avg `0.0426` n `20`; unknown avg `0.7852` n `794`
- 24h: commodity avg `-0.0443` n `12`; crypto_alt avg `2.0729` n `230`; crypto_major avg `2.4761` n `8`; equity avg `-1.0244` n `121`; fx avg `0.0396` n `6`; index avg `-0.1146` n `25`; metal avg `-0.0825` n `20`; unknown avg `1.5264` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
