# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T19:22:19.730800+00:00`
- Correlation status: `ready`
- Asset price records: `577`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5706` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1656` n `12`; crypto_alt avg `0.0175` n `228`; crypto_major avg `-0.0228` n `8`; equity avg `0.0403` n `65`; fx avg `0.0067` n `5`; index avg `-0.0012` n `23`; metal avg `-0.1522` n `18`; unknown avg `-0.1758` n `365`
- 1h: commodity avg `0.5081` n `12`; crypto_alt avg `-0.2315` n `228`; crypto_major avg `-0.3536` n `8`; equity avg `-0.2249` n `65`; fx avg `0.0201` n `5`; index avg `-0.1774` n `23`; metal avg `-0.3509` n `18`; unknown avg `-0.3915` n `365`
- 4h: commodity avg `1.5591` n `12`; crypto_alt avg `1.2228` n `228`; crypto_major avg `-0.0028` n `8`; equity avg `-1.3171` n `65`; fx avg `0.0382` n `5`; index avg `-0.8544` n `23`; metal avg `-1.5734` n `18`; unknown avg `-0.2714` n `365`
- 24h: commodity avg `0.8873` n `12`; crypto_alt avg `1.223` n `228`; crypto_major avg `-1.9924` n `8`; equity avg `-1.3956` n `65`; fx avg `0.1893` n `5`; index avg `-0.9307` n `23`; metal avg `-0.0456` n `18`; unknown avg `-0.3241` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1414`, n `573`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `573`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `573`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `573`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `569`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `569`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0938`, n `569`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0892`, n `569`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0879`, n `569`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0867`, n `569`, weak_sample_signal
