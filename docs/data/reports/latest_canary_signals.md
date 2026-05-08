# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T18:22:11.532857+00:00`
- Correlation status: `ready`
- Asset price records: `669`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0411` n `12`; crypto_alt avg `0.2685` n `228`; crypto_major avg `0.2313` n `8`; equity avg `0.1117` n `65`; fx avg `-0.0011` n `5`; index avg `0.0019` n `23`; metal avg `0.0194` n `18`; unknown avg `-0.16` n `375`
- 1h: commodity avg `-0.2416` n `12`; crypto_alt avg `0.7871` n `228`; crypto_major avg `0.8884` n `8`; equity avg `0.4414` n `65`; fx avg `0.0105` n `5`; index avg `0.1686` n `23`; metal avg `0.282` n `18`; unknown avg `0.2382` n `375`
- 4h: commodity avg `-0.2262` n `12`; crypto_alt avg `1.7462` n `228`; crypto_major avg `1.1416` n `8`; equity avg `0.5491` n `65`; fx avg `-0.0067` n `5`; index avg `0.4078` n `23`; metal avg `0.2298` n `18`; unknown avg `-0.0819` n `375`
- 24h: commodity avg `0.2906` n `12`; crypto_alt avg `3.0915` n `228`; crypto_major avg `1.1027` n `8`; equity avg `2.9509` n `65`; fx avg `0.1903` n `5`; index avg `1.4787` n `23`; metal avg `0.7436` n `18`; unknown avg `0.3372` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1217`, n `661`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1175`, n `661`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1097`, n `665`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0959`, n `661`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0955`, n `665`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0935`, n `661`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0691`, n `665`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `665`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0656`, n `661`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0611`, n `665`, weak_sample_signal
