# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T12:11:14.158694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1802` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `0.5002` n `230`; crypto_major avg `0.7059` n `8`; equity avg `0.0339` n `121`; fx avg `-0.0063` n `6`; index avg `0.0039` n `25`; metal avg `0.0045` n `20`; unknown avg `0.121` n `794`
- 1h: commodity avg `-0.0005` n `12`; crypto_alt avg `0.7957` n `230`; crypto_major avg `0.8477` n `8`; equity avg `0.0921` n `121`; fx avg `-0.0019` n `6`; index avg `0.0105` n `25`; metal avg `0.0319` n `20`; unknown avg `0.2151` n `794`
- 4h: commodity avg `-0.0244` n `12`; crypto_alt avg `-1.3806` n `230`; crypto_major avg `-1.1758` n `8`; equity avg `-0.0939` n `121`; fx avg `0.028` n `6`; index avg `0.0044` n `25`; metal avg `0.0257` n `20`; unknown avg `0.1076` n `794`
- 24h: commodity avg `0.0117` n `12`; crypto_alt avg `2.316` n `230`; crypto_major avg `4.4155` n `8`; equity avg `-0.8899` n `121`; fx avg `0.0458` n `6`; index avg `-0.1203` n `25`; metal avg `-0.1766` n `20`; unknown avg `1.5254` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
