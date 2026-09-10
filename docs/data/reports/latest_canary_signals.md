# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T15:52:35.991054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1757` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1335` n `12`; crypto_alt avg `-0.2696` n `233`; crypto_major avg `-0.2699` n `8`; equity avg `-0.109` n `135`; fx avg `0.0233` n `6`; index avg `-0.0332` n `26`; metal avg `-0.0216` n `20`; unknown avg `-0.2006` n `796`
- 1h: commodity avg `0.2422` n `12`; crypto_alt avg `-0.0627` n `233`; crypto_major avg `-0.265` n `8`; equity avg `-0.096` n `135`; fx avg `0.0144` n `6`; index avg `-0.0229` n `26`; metal avg `-0.0025` n `20`; unknown avg `-0.2851` n `794`
- 4h: commodity avg `0.594` n `12`; crypto_alt avg `-0.7423` n `233`; crypto_major avg `-1.367` n `8`; equity avg `-0.3144` n `135`; fx avg `0.0413` n `6`; index avg `-0.1913` n `26`; metal avg `-0.3033` n `20`; unknown avg `-0.8641` n `760`
- 24h: commodity avg `0.629` n `12`; crypto_alt avg `-3.9587` n `233`; crypto_major avg `-3.4377` n `8`; equity avg `-1.6271` n `135`; fx avg `0.1134` n `6`; index avg `-0.2767` n `26`; metal avg `-1.042` n `20`; unknown avg `-0.7868` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
