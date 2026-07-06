# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T01:37:26.796057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.36` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.6318` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0778` n `12`; crypto_alt avg `0.1027` n `229`; crypto_major avg `0.1133` n `8`; equity avg `-0.3158` n `88`; fx avg `0.0185` n `6`; index avg `-0.034` n `25`; metal avg `0.1138` n `20`; unknown avg `-0.0071` n `765`
- 1h: commodity avg `-0.0438` n `12`; crypto_alt avg `0.5381` n `229`; crypto_major avg `0.6541` n `8`; equity avg `-0.3888` n `88`; fx avg `0.0071` n `6`; index avg `-0.0585` n `25`; metal avg `0.0949` n `20`; unknown avg `0.2112` n `765`
- 4h: commodity avg `-0.258` n `12`; crypto_alt avg `0.3611` n `229`; crypto_major avg `0.9851` n `8`; equity avg `-0.6467` n `88`; fx avg `0.1089` n `6`; index avg `0.0005` n `25`; metal avg `0.1547` n `20`; unknown avg `1.089` n `765`
- 24h: commodity avg `-0.2573` n `12`; crypto_alt avg `0.9666` n `229`; crypto_major avg `2.1488` n `8`; equity avg `-0.3116` n `88`; fx avg `0.0532` n `6`; index avg `0.1081` n `25`; metal avg `0.1617` n `20`; unknown avg `1.5874` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
