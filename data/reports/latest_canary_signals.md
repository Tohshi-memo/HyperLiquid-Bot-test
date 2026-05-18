# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T09:52:17.718709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `-0.1605` n `228`; crypto_major avg `-0.1968` n `8`; equity avg `-0.0271` n `66`; fx avg `0.0237` n `5`; index avg `-0.0122` n `23`; metal avg `-0.0834` n `18`; unknown avg `-0.035` n `383`
- 1h: commodity avg `0.0819` n `12`; crypto_alt avg `-0.2285` n `228`; crypto_major avg `-0.3061` n `8`; equity avg `-0.126` n `66`; fx avg `0.0493` n `5`; index avg `-0.0659` n `23`; metal avg `-0.3363` n `18`; unknown avg `-0.4503` n `383`
- 4h: commodity avg `-0.0835` n `12`; crypto_alt avg `-0.6624` n `228`; crypto_major avg `-0.6185` n `8`; equity avg `0.6094` n `66`; fx avg `0.0018` n `5`; index avg `0.1928` n `23`; metal avg `0.3707` n `18`; unknown avg `-0.2219` n `363`
- 24h: commodity avg `0.6472` n `12`; crypto_alt avg `-3.1875` n `228`; crypto_major avg `-1.7997` n `8`; equity avg `0.3938` n `65`; fx avg `0.0854` n `5`; index avg `0.2631` n `23`; metal avg `-0.0387` n `18`; unknown avg `-0.6682` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
