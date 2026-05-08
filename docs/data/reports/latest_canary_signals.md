# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T12:37:10.575086+00:00`
- Correlation status: `ready`
- Asset price records: `646`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0228` n `12`; crypto_alt avg `-0.0773` n `228`; crypto_major avg `0.0247` n `8`; equity avg `0.213` n `65`; fx avg `-0.0134` n `5`; index avg `0.1803` n `23`; metal avg `0.3726` n `18`; unknown avg `-0.084` n `375`
- 1h: commodity avg `0.0435` n `12`; crypto_alt avg `-0.1236` n `228`; crypto_major avg `0.0652` n `8`; equity avg `0.2286` n `65`; fx avg `-0.0216` n `5`; index avg `0.2228` n `23`; metal avg `0.1669` n `18`; unknown avg `0.1186` n `375`
- 4h: commodity avg `0.1572` n `12`; crypto_alt avg `0.3021` n `228`; crypto_major avg `0.2761` n `8`; equity avg `0.2725` n `65`; fx avg `0.0118` n `5`; index avg `0.2397` n `23`; metal avg `0.2255` n `18`; unknown avg `0.1346` n `375`
- 24h: commodity avg `2.0755` n `12`; crypto_alt avg `0.3687` n `228`; crypto_major avg `-1.4786` n `8`; equity avg `-0.2625` n `65`; fx avg `0.2553` n `5`; index avg `-0.1961` n `23`; metal avg `-0.5384` n `18`; unknown avg `-0.0252` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1333`, n `638`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1328`, n `638`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1088`, n `642`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `642`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `642`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `642`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0867`, n `638`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0857`, n `638`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `642`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `642`, weak_sample_signal
