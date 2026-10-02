# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T21:52:29.281586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.394` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0113` n `13`; crypto_alt avg `0.2142` n `235`; crypto_major avg `0.0789` n `8`; equity avg `0.0071` n `143`; fx avg `-0.005` n `6`; index avg `0.0141` n `26`; metal avg `-0.0063` n `20`; unknown avg `0.074` n `968`
- 1h: commodity avg `0.0944` n `13`; crypto_alt avg `0.2101` n `235`; crypto_major avg `0.094` n `8`; equity avg `0.0167` n `143`; fx avg `0.0028` n `6`; index avg `0.0158` n `26`; metal avg `0.0353` n `20`; unknown avg `0.0615` n `964`
- 4h: commodity avg `0.3386` n `13`; crypto_alt avg `-2.2711` n `235`; crypto_major avg `-1.3604` n `8`; equity avg `-0.0008` n `143`; fx avg `-0.0247` n `6`; index avg `0.0336` n `26`; metal avg `0.0971` n `20`; unknown avg `7.9861` n `906`
- 24h: commodity avg `0.0081` n `13`; crypto_alt avg `-0.929` n `235`; crypto_major avg `-0.5472` n `8`; equity avg `0.7991` n `142`; fx avg `-0.1592` n `6`; index avg `0.3168` n `26`; metal avg `-0.2445` n `20`; unknown avg `-0.3931` n `810`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
