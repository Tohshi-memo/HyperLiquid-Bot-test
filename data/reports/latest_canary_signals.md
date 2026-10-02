# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T21:07:32.406880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7036` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6613` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.6191` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0296` n `13`; crypto_alt avg `-0.0986` n `235`; crypto_major avg `0.0154` n `8`; equity avg `0.0348` n `143`; fx avg `0.0035` n `6`; index avg `0.0073` n `26`; metal avg `0.0293` n `20`; unknown avg `17.3312` n `980`
- 1h: commodity avg `-0.0308` n `13`; crypto_alt avg `-0.0367` n `235`; crypto_major avg `-0.0308` n `8`; equity avg `-0.0251` n `143`; fx avg `-0.0157` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0278` n `20`; unknown avg `21.5342` n `940`
- 4h: commodity avg `0.2033` n `13`; crypto_alt avg `-3.0024` n `235`; crypto_major avg `-1.5998` n `8`; equity avg `0.0615` n `143`; fx avg `-0.0138` n `6`; index avg `0.0193` n `26`; metal avg `0.1038` n `20`; unknown avg `4.9893` n `922`
- 24h: commodity avg `-0.0403` n `13`; crypto_alt avg `-1.832` n `235`; crypto_major avg `-1.0461` n `8`; equity avg `0.7354` n `142`; fx avg `-0.1377` n `6`; index avg `0.2997` n `26`; metal avg `-0.256` n `20`; unknown avg `-0.2255` n `802`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
