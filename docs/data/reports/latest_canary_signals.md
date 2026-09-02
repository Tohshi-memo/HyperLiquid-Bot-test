# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T09:37:29.724034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3654` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0169` n `12`; crypto_alt avg `-0.3098` n `232`; crypto_major avg `-0.3597` n `8`; equity avg `-0.1789` n `132`; fx avg `0.0134` n `6`; index avg `-0.023` n `26`; metal avg `-0.04` n `20`; unknown avg `-0.121` n `792`
- 1h: commodity avg `0.0547` n `12`; crypto_alt avg `-0.7585` n `232`; crypto_major avg `-0.7596` n `8`; equity avg `-0.5186` n `132`; fx avg `0.0177` n `6`; index avg `-0.1135` n `26`; metal avg `-0.1209` n `20`; unknown avg `-0.177` n `790`
- 4h: commodity avg `-0.092` n `12`; crypto_alt avg `-1.1456` n `232`; crypto_major avg `-1.5048` n `8`; equity avg `-0.8056` n `132`; fx avg `-0.0552` n `6`; index avg `-0.1394` n `26`; metal avg `-0.1295` n `20`; unknown avg `-0.1274` n `770`
- 24h: commodity avg `0.5539` n `12`; crypto_alt avg `-0.4276` n `232`; crypto_major avg `-2.0534` n `8`; equity avg `-1.7722` n `130`; fx avg `-0.2038` n `6`; index avg `-0.2893` n `26`; metal avg `-0.4362` n `20`; unknown avg `-0.4758` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0458`, n `668`, weak_sample_signal
