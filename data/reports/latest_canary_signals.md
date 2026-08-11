# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T02:22:28.791070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `-0.0605` n `230`; crypto_major avg `-0.0295` n `8`; equity avg `0.0017` n `113`; fx avg `0.0063` n `6`; index avg `-0.0061` n `25`; metal avg `0.0238` n `20`; unknown avg `-0.0477` n `785`
- 1h: commodity avg `0.0218` n `12`; crypto_alt avg `0.0915` n `230`; crypto_major avg `0.1403` n `8`; equity avg `-0.1373` n `113`; fx avg `0.0335` n `6`; index avg `-0.0026` n `25`; metal avg `0.0132` n `20`; unknown avg `-0.1592` n `785`
- 4h: commodity avg `0.0231` n `12`; crypto_alt avg `0.3037` n `230`; crypto_major avg `0.1167` n `8`; equity avg `0.2662` n `113`; fx avg `-0.021` n `6`; index avg `0.0916` n `25`; metal avg `0.2039` n `20`; unknown avg `-0.2949` n `785`
- 24h: commodity avg `0.8393` n `12`; crypto_alt avg `-0.2467` n `230`; crypto_major avg `-0.4112` n `8`; equity avg `-1.0437` n `113`; fx avg `0.1271` n `6`; index avg `0.0079` n `25`; metal avg `0.6369` n `20`; unknown avg `103.7958` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
