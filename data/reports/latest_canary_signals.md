# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T16:07:32.478495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3079` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0594` n `12`; crypto_alt avg `-0.3961` n `233`; crypto_major avg `-0.2521` n `8`; equity avg `-0.2231` n `135`; fx avg `-0.0099` n `6`; index avg `-0.0327` n `26`; metal avg `-0.0437` n `20`; unknown avg `-0.1465` n `794`
- 1h: commodity avg `0.2666` n `12`; crypto_alt avg `-0.4313` n `233`; crypto_major avg `-0.5357` n `8`; equity avg `-0.3507` n `135`; fx avg `0.0159` n `6`; index avg `-0.0724` n `26`; metal avg `-0.0416` n `20`; unknown avg `-0.3151` n `794`
- 4h: commodity avg `0.4079` n `12`; crypto_alt avg `-0.9045` n `233`; crypto_major avg `-1.4805` n `8`; equity avg `-0.3053` n `135`; fx avg `0.0267` n `6`; index avg `-0.1726` n `26`; metal avg `-0.3115` n `20`; unknown avg `-0.7569` n `760`
- 24h: commodity avg `0.6464` n `12`; crypto_alt avg `-4.4398` n `233`; crypto_major avg `-3.7558` n `8`; equity avg `-1.8231` n `135`; fx avg `0.1252` n `6`; index avg `-0.2838` n `26`; metal avg `-1.0516` n `20`; unknown avg `-0.5503` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
