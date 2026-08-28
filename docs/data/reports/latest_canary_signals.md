# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T15:22:30.264372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.035` n `12`; crypto_alt avg `0.1669` n `231`; crypto_major avg `0.2033` n `8`; equity avg `-0.0154` n `127`; fx avg `-0.0101` n `6`; index avg `-0.0164` n `26`; metal avg `-0.1128` n `20`; unknown avg `0.0233` n `793`
- 1h: commodity avg `0.0515` n `12`; crypto_alt avg `0.8787` n `231`; crypto_major avg `0.877` n `8`; equity avg `-0.0359` n `127`; fx avg `0.0173` n `6`; index avg `0.051` n `26`; metal avg `0.1302` n `20`; unknown avg `0.2464` n `793`
- 4h: commodity avg `-0.0439` n `12`; crypto_alt avg `-0.1474` n `231`; crypto_major avg `-0.0062` n `8`; equity avg `-0.3396` n `127`; fx avg `-0.0354` n `6`; index avg `0.0792` n `26`; metal avg `-0.0116` n `20`; unknown avg `-0.1079` n `792`
- 24h: commodity avg `0.0245` n `12`; crypto_alt avg `-1.1676` n `231`; crypto_major avg `-1.019` n `8`; equity avg `-0.6549` n `127`; fx avg `-0.0784` n `6`; index avg `0.1152` n `26`; metal avg `0.6384` n `20`; unknown avg `0.2165` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
