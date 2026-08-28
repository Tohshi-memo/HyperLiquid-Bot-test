# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T13:07:33.332534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0449` n `12`; crypto_alt avg `0.1148` n `231`; crypto_major avg `0.1663` n `8`; equity avg `0.0308` n `127`; fx avg `0.0034` n `6`; index avg `0.0094` n `26`; metal avg `0.1176` n `20`; unknown avg `-0.1198` n `792`
- 1h: commodity avg `-0.0436` n `12`; crypto_alt avg `-0.1537` n `231`; crypto_major avg `-0.0964` n `8`; equity avg `0.1491` n `127`; fx avg `-0.0177` n `6`; index avg `0.038` n `26`; metal avg `0.1252` n `20`; unknown avg `-0.1962` n `792`
- 4h: commodity avg `-0.2607` n `12`; crypto_alt avg `0.176` n `231`; crypto_major avg `-0.115` n `8`; equity avg `0.0822` n `127`; fx avg `0.0241` n `6`; index avg `0.032` n `26`; metal avg `0.2324` n `20`; unknown avg `0.0067` n `792`
- 24h: commodity avg `-0.1301` n `12`; crypto_alt avg `-0.541` n `231`; crypto_major avg `-0.0175` n `8`; equity avg `-0.7432` n `127`; fx avg `-0.0751` n `6`; index avg `0.0285` n `26`; metal avg `0.9391` n `20`; unknown avg `0.5229` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
