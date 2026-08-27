# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T13:37:32.984530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0975` n `12`; crypto_alt avg `-0.2363` n `231`; crypto_major avg `-0.2177` n `8`; equity avg `-0.1836` n `127`; fx avg `0.0021` n `6`; index avg `-0.0587` n `26`; metal avg `-0.064` n `20`; unknown avg `-0.0044` n `792`
- 1h: commodity avg `0.153` n `12`; crypto_alt avg `0.2145` n `231`; crypto_major avg `0.0776` n `8`; equity avg `-0.2808` n `127`; fx avg `0.057` n `6`; index avg `-0.0708` n `26`; metal avg `-0.0602` n `20`; unknown avg `-0.1025` n `792`
- 4h: commodity avg `0.2537` n `12`; crypto_alt avg `-0.8094` n `231`; crypto_major avg `-1.0137` n `8`; equity avg `-0.5819` n `127`; fx avg `0.0489` n `6`; index avg `-0.0912` n `26`; metal avg `-0.0563` n `20`; unknown avg `0.0792` n `792`
- 24h: commodity avg `0.4843` n `12`; crypto_alt avg `1.7874` n `231`; crypto_major avg `2.0533` n `8`; equity avg `1.4105` n `127`; fx avg `-0.0319` n `6`; index avg `0.1888` n `26`; metal avg `-0.3814` n `20`; unknown avg `0.427` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
