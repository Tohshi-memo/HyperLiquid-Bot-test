# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T20:52:25.273014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `0.0494` n `231`; crypto_major avg `0.0606` n `8`; equity avg `0.0291` n `127`; fx avg `-0.029` n `6`; index avg `0.0113` n `26`; metal avg `0.0254` n `20`; unknown avg `0.053` n `793`
- 1h: commodity avg `0.0154` n `12`; crypto_alt avg `0.2151` n `231`; crypto_major avg `0.1023` n `8`; equity avg `0.0333` n `127`; fx avg `-0.0452` n `6`; index avg `-0.0016` n `26`; metal avg `0.0298` n `20`; unknown avg `-0.0219` n `793`
- 4h: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.4011` n `231`; crypto_major avg `-0.9297` n `8`; equity avg `-0.2302` n `127`; fx avg `-0.0736` n `6`; index avg `-0.0704` n `26`; metal avg `-0.2133` n `20`; unknown avg `-0.4551` n `793`
- 24h: commodity avg `-0.107` n `12`; crypto_alt avg `-3.2221` n `231`; crypto_major avg `-3.6047` n `8`; equity avg `-2.2717` n `127`; fx avg `-0.1622` n `6`; index avg `-0.1834` n `26`; metal avg `-0.3691` n `20`; unknown avg `-0.6644` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
