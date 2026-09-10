# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T13:37:30.481542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1258` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.069` n `12`; crypto_alt avg `0.2472` n `233`; crypto_major avg `0.1816` n `8`; equity avg `0.449` n `134`; fx avg `0.01` n `6`; index avg `0.0133` n `26`; metal avg `0.0396` n `20`; unknown avg `1.8917` n `797`
- 1h: commodity avg `-0.0933` n `12`; crypto_alt avg `-0.2558` n `233`; crypto_major avg `-0.6428` n `8`; equity avg `0.0875` n `134`; fx avg `-0.017` n `6`; index avg `-0.0469` n `26`; metal avg `0.1476` n `20`; unknown avg `33.7151` n `795`
- 4h: commodity avg `0.3465` n `12`; crypto_alt avg `-0.8422` n `233`; crypto_major avg `-1.3884` n `8`; equity avg `-1.0316` n `134`; fx avg `0.0053` n `6`; index avg `-0.2626` n `26`; metal avg `-0.7046` n `20`; unknown avg `0.2879` n `789`
- 24h: commodity avg `0.3947` n `12`; crypto_alt avg `-5.021` n `233`; crypto_major avg `-4.2475` n `8`; equity avg `-2.3699` n `134`; fx avg `0.0883` n `6`; index avg `-0.3421` n `26`; metal avg `-1.0672` n `20`; unknown avg `-1.0713` n `669`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
