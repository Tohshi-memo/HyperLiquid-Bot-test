# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T12:07:24.021741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1988` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0409` n `12`; crypto_alt avg `0.0566` n `232`; crypto_major avg `0.0572` n `8`; equity avg `0.3277` n `132`; fx avg `-0.0181` n `6`; index avg `0.0574` n `26`; metal avg `0.0517` n `20`; unknown avg `0.456` n `790`
- 1h: commodity avg `-0.2448` n `12`; crypto_alt avg `0.3308` n `232`; crypto_major avg `0.2911` n `8`; equity avg `0.7094` n `132`; fx avg `-0.0447` n `6`; index avg `0.1551` n `26`; metal avg `0.2606` n `20`; unknown avg `0.4353` n `790`
- 4h: commodity avg `-0.2082` n `12`; crypto_alt avg `-1.3695` n `232`; crypto_major avg `-1.1807` n `8`; equity avg `-0.1154` n `132`; fx avg `-0.0824` n `6`; index avg `0.0181` n `26`; metal avg `0.1732` n `20`; unknown avg `0.2076` n `790`
- 24h: commodity avg `0.3604` n `12`; crypto_alt avg `-1.5829` n `232`; crypto_major avg `-2.4365` n `8`; equity avg `-1.0586` n `130`; fx avg `-0.2846` n `6`; index avg `-0.1253` n `26`; metal avg `-0.1649` n `20`; unknown avg `-0.1802` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
