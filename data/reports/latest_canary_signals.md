# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T00:37:29.902342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1837` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0153` n `13`; crypto_alt avg `-0.1545` n `239`; crypto_major avg `-0.1721` n `8`; equity avg `-0.0695` n `162`; fx avg `-0.0004` n `6`; index avg `0.0145` n `27`; metal avg `-0.0084` n `20`; unknown avg `1.4863` n `1262`
- 1h: commodity avg `0.0465` n `13`; crypto_alt avg `0.0014` n `239`; crypto_major avg `0.2186` n `8`; equity avg `0.0565` n `162`; fx avg `-0.013` n `6`; index avg `0.0106` n `27`; metal avg `-0.0034` n `20`; unknown avg `1.7741` n `1254`
- 4h: commodity avg `0.0627` n `13`; crypto_alt avg `-0.9467` n `239`; crypto_major avg `-1.2228` n `8`; equity avg `-0.8476` n `162`; fx avg `-0.0241` n `6`; index avg `-0.0391` n `27`; metal avg `0.0012` n `20`; unknown avg `4.4194` n `1166`
- 24h: commodity avg `-0.1985` n `13`; crypto_alt avg `-1.4223` n `239`; crypto_major avg `-2.7048` n `8`; equity avg `-3.8456` n `162`; fx avg `-0.0981` n `6`; index avg `-0.3081` n `27`; metal avg `-0.3728` n `20`; unknown avg `61.4301` n `1035`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
