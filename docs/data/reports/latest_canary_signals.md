# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T09:52:32.328418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2951` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0083` n `12`; crypto_alt avg `0.0627` n `232`; crypto_major avg `0.1575` n `8`; equity avg `0.0335` n `132`; fx avg `-0.0104` n `6`; index avg `0.0008` n `26`; metal avg `0.0039` n `20`; unknown avg `0.1362` n `792`
- 1h: commodity avg `0.0081` n `12`; crypto_alt avg `-0.2065` n `232`; crypto_major avg `-0.1081` n `8`; equity avg `-0.268` n `132`; fx avg `-0.0033` n `6`; index avg `-0.0647` n `26`; metal avg `-0.0598` n `20`; unknown avg `-0.0192` n `790`
- 4h: commodity avg `-0.0784` n `12`; crypto_alt avg `-1.1539` n `232`; crypto_major avg `-1.4366` n `8`; equity avg `-0.7968` n `132`; fx avg `-0.0507` n `6`; index avg `-0.1415` n `26`; metal avg `-0.1467` n `20`; unknown avg `-0.3413` n `770`
- 24h: commodity avg `0.5569` n `12`; crypto_alt avg `-0.462` n `232`; crypto_major avg `-1.9117` n `8`; equity avg `-1.8916` n `130`; fx avg `-0.2137` n `6`; index avg `-0.3096` n `26`; metal avg `-0.4403` n `20`; unknown avg `-0.3655` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0458`, n `668`, weak_sample_signal
