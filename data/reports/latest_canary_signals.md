# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T14:52:26.371070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1225` n `12`; crypto_alt avg `-0.2329` n `233`; crypto_major avg `-0.1503` n `8`; equity avg `-0.153` n `135`; fx avg `0.0169` n `6`; index avg `-0.051` n `26`; metal avg `-0.0993` n `20`; unknown avg `-0.1053` n `768`
- 1h: commodity avg `0.0825` n `12`; crypto_alt avg `0.0575` n `233`; crypto_major avg `0.0704` n `8`; equity avg `0.528` n `135`; fx avg `0.0271` n `6`; index avg `0.055` n `26`; metal avg `-0.1312` n `20`; unknown avg `-0.1616` n `766`
- 4h: commodity avg `0.4748` n `12`; crypto_alt avg `-0.5834` n `233`; crypto_major avg `-1.098` n `8`; equity avg `-0.4868` n `135`; fx avg `0.0186` n `6`; index avg `-0.2396` n `26`; metal avg `-0.4102` n `20`; unknown avg `-0.467` n `760`
- 24h: commodity avg `0.3434` n `12`; crypto_alt avg `-4.7352` n `233`; crypto_major avg `-3.7669` n `8`; equity avg `-1.7506` n `135`; fx avg `0.107` n `6`; index avg `-0.3275` n `26`; metal avg `-1.182` n `20`; unknown avg `-0.7051` n `660`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
