# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T21:41:40.035786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.366` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `-0.9617` n `230`; crypto_major avg `-0.7336` n `8`; equity avg `-0.0228` n `121`; fx avg `-0.0161` n `6`; index avg `-0.0011` n `25`; metal avg `0.0195` n `20`; unknown avg `-0.2234` n `794`
- 1h: commodity avg `0.0339` n `12`; crypto_alt avg `-1.6745` n `230`; crypto_major avg `-1.3706` n `8`; equity avg `-0.0528` n `121`; fx avg `0.0011` n `6`; index avg `-0.0046` n `25`; metal avg `0.0256` n `20`; unknown avg `-0.1552` n `794`
- 4h: commodity avg `0.0959` n `12`; crypto_alt avg `-1.7164` n `230`; crypto_major avg `-0.4609` n `8`; equity avg `0.0852` n `121`; fx avg `0.0345` n `6`; index avg `-0.0054` n `25`; metal avg `0.0225` n `20`; unknown avg `1.081` n `794`
- 24h: commodity avg `0.0723` n `12`; crypto_alt avg `-2.0661` n `230`; crypto_major avg `0.692` n `8`; equity avg `-0.4221` n `121`; fx avg `0.065` n `6`; index avg `-0.0488` n `25`; metal avg `-0.0653` n `20`; unknown avg `2.9725` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
