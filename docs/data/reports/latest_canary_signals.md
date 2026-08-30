# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T19:37:30.940203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `12`; crypto_alt avg `-0.2233` n `231`; crypto_major avg `-0.1993` n `8`; equity avg `-0.0154` n `128`; fx avg `-0.0037` n `6`; index avg `-0.0078` n `26`; metal avg `-0.007` n `20`; unknown avg `0.2258` n `793`
- 1h: commodity avg `0.1489` n `12`; crypto_alt avg `-0.3421` n `231`; crypto_major avg `-0.6054` n `8`; equity avg `-0.0443` n `128`; fx avg `-0.0071` n `6`; index avg `-0.0132` n `26`; metal avg `-0.0099` n `20`; unknown avg `0.3165` n `793`
- 4h: commodity avg `0.1863` n `12`; crypto_alt avg `0.4101` n `231`; crypto_major avg `0.1615` n `8`; equity avg `0.0907` n `128`; fx avg `-0.0034` n `6`; index avg `0.0058` n `26`; metal avg `0.0325` n `20`; unknown avg `0.2612` n `793`
- 24h: commodity avg `0.1982` n `12`; crypto_alt avg `1.4386` n `231`; crypto_major avg `0.7343` n `8`; equity avg `0.2272` n `128`; fx avg `0.0341` n `6`; index avg `0.0538` n `26`; metal avg `0.1025` n `20`; unknown avg `0.0573` n `740`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
