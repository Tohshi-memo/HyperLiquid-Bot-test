# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T05:22:29.160963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0659` n `12`; crypto_alt avg `0.0647` n `230`; crypto_major avg `0.108` n `8`; equity avg `-0.1321` n `98`; fx avg `0.0098` n `6`; index avg `-0.0688` n `25`; metal avg `0.0051` n `20`; unknown avg `-0.1703` n `771`
- 1h: commodity avg `0.0649` n `12`; crypto_alt avg `0.1532` n `230`; crypto_major avg `0.1414` n `8`; equity avg `-0.147` n `98`; fx avg `0.0177` n `6`; index avg `-0.089` n `25`; metal avg `0.0152` n `20`; unknown avg `-0.0825` n `771`
- 4h: commodity avg `0.0711` n `12`; crypto_alt avg `0.5511` n `230`; crypto_major avg `0.5243` n `8`; equity avg `0.7036` n `98`; fx avg `-0.0304` n `6`; index avg `0.1182` n `25`; metal avg `0.2172` n `20`; unknown avg `0.2616` n `771`
- 24h: commodity avg `-0.2709` n `12`; crypto_alt avg `2.9142` n `230`; crypto_major avg `2.4387` n `8`; equity avg `1.1273` n `98`; fx avg `-0.1095` n `6`; index avg `0.2308` n `25`; metal avg `0.4199` n `20`; unknown avg `0.1501` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.146`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1197`, n `669`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.11`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `667`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0873`, n `667`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0822`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0721`, n `667`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0714`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.07`, n `667`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0665`, n `667`, weak_sample_signal
