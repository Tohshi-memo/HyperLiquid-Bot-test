# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T11:52:33.466664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0282` n `12`; crypto_alt avg `-0.0614` n `228`; crypto_major avg `-0.117` n `8`; equity avg `0.0543` n `74`; fx avg `0.0071` n `6`; index avg `0.1409` n `23`; metal avg `-0.0058` n `18`; unknown avg `-0.0346` n `516`
- 1h: commodity avg `0.0081` n `12`; crypto_alt avg `0.4929` n `228`; crypto_major avg `0.2613` n `8`; equity avg `0.3065` n `74`; fx avg `0.0158` n `6`; index avg `0.1076` n `23`; metal avg `0.0166` n `18`; unknown avg `0.0263` n `516`
- 4h: commodity avg `0.0245` n `12`; crypto_alt avg `0.1872` n `228`; crypto_major avg `0.188` n `8`; equity avg `0.0159` n `74`; fx avg `-0.0196` n `6`; index avg `-0.0606` n `23`; metal avg `-0.0051` n `18`; unknown avg `-4.8143` n `516`
- 24h: commodity avg `0.0755` n `12`; crypto_alt avg `2.9224` n `228`; crypto_major avg `2.6448` n `8`; equity avg `2.0096` n `74`; fx avg `0.0197` n `6`; index avg `0.8177` n `23`; metal avg `0.5608` n `18`; unknown avg `0.0809` n `403`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
