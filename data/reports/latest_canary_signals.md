# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T13:07:26.072100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `0.068` n `230`; crypto_major avg `-0.0441` n `8`; equity avg `0.1283` n `113`; fx avg `0.0128` n `6`; index avg `0.0169` n `25`; metal avg `-0.0579` n `20`; unknown avg `0.0026` n `784`
- 1h: commodity avg `0.079` n `12`; crypto_alt avg `-0.1156` n `230`; crypto_major avg `-0.4666` n `8`; equity avg `-0.3971` n `113`; fx avg `0.0391` n `6`; index avg `-0.0384` n `25`; metal avg `-0.0623` n `20`; unknown avg `0.0425` n `784`
- 4h: commodity avg `0.146` n `12`; crypto_alt avg `0.0637` n `230`; crypto_major avg `-0.3382` n `8`; equity avg `-0.7772` n `113`; fx avg `-0.0094` n `6`; index avg `-0.1104` n `25`; metal avg `-0.0954` n `20`; unknown avg `-0.1041` n `784`
- 24h: commodity avg `0.6904` n `12`; crypto_alt avg `0.6923` n `230`; crypto_major avg `-0.2186` n `8`; equity avg `-0.8229` n `113`; fx avg `0.2399` n `6`; index avg `-0.0331` n `25`; metal avg `-0.1933` n `20`; unknown avg `56.977` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
