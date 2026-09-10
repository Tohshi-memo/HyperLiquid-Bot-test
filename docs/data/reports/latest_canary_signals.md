# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T15:37:34.683659+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0787` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `0.3731` n `233`; crypto_major avg `0.1962` n `8`; equity avg `0.1662` n `135`; fx avg `0.0027` n `6`; index avg `0.032` n `26`; metal avg `0.0038` n `20`; unknown avg `0.0871` n `796`
- 1h: commodity avg `0.2312` n `12`; crypto_alt avg `-0.0265` n `233`; crypto_major avg `-0.1455` n `8`; equity avg `-0.1391` n `135`; fx avg `0.0079` n `6`; index avg `-0.0407` n `26`; metal avg `-0.0802` n `20`; unknown avg `-0.3549` n `766`
- 4h: commodity avg `0.5728` n `12`; crypto_alt avg `-0.7924` n `233`; crypto_major avg `-1.2873` n `8`; equity avg `-0.4171` n `135`; fx avg `0.0013` n `6`; index avg `-0.2086` n `26`; metal avg `-0.3687` n `20`; unknown avg `-0.8983` n `760`
- 24h: commodity avg `0.4443` n `12`; crypto_alt avg `-3.5297` n `233`; crypto_major avg `-3.1394` n `8`; equity avg `-1.3633` n `135`; fx avg `0.0864` n `6`; index avg `-0.2297` n `26`; metal avg `-0.9988` n `20`; unknown avg `-1.2204` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
