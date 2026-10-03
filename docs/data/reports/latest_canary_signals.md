# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T03:07:32.229334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `13`; crypto_alt avg `-0.0354` n `235`; crypto_major avg `-0.1543` n `8`; equity avg `-0.0226` n `143`; fx avg `-0.0123` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0022` n `20`; unknown avg `-0.1528` n `982`
- 1h: commodity avg `0.0116` n `13`; crypto_alt avg `0.0588` n `235`; crypto_major avg `-0.1485` n `8`; equity avg `-0.0154` n `143`; fx avg `-0.001` n `6`; index avg `-0.0025` n `26`; metal avg `0.0018` n `20`; unknown avg `-0.2404` n `982`
- 4h: commodity avg `-0.2122` n `13`; crypto_alt avg `0.8381` n `235`; crypto_major avg `0.2325` n `8`; equity avg `0.0335` n `143`; fx avg `0.0086` n `6`; index avg `0.0325` n `26`; metal avg `-0.0236` n `20`; unknown avg `-0.1535` n `976`
- 24h: commodity avg `0.0999` n `13`; crypto_alt avg `-0.8203` n `235`; crypto_major avg `-0.9648` n `8`; equity avg `0.5789` n `142`; fx avg `-0.1237` n `6`; index avg `0.268` n `26`; metal avg `-0.2192` n `20`; unknown avg `-0.7532` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
