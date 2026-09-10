# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T19:22:35.494469+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0563` n `12`; crypto_alt avg `-0.0106` n `233`; crypto_major avg `0.0059` n `8`; equity avg `0.0111` n `135`; fx avg `0.0141` n `6`; index avg `0.004` n `26`; metal avg `0.0345` n `20`; unknown avg `-0.1832` n `797`
- 1h: commodity avg `-0.0109` n `12`; crypto_alt avg `0.1086` n `233`; crypto_major avg `0.2429` n `8`; equity avg `-0.1127` n `135`; fx avg `0.0188` n `6`; index avg `-0.0204` n `26`; metal avg `-0.102` n `20`; unknown avg `0.237` n `795`
- 4h: commodity avg `0.4436` n `12`; crypto_alt avg `0.1504` n `233`; crypto_major avg `0.2031` n `8`; equity avg `-0.6169` n `135`; fx avg `0.0367` n `6`; index avg `-0.0891` n `26`; metal avg `-0.3094` n `20`; unknown avg `0.0934` n `788`
- 24h: commodity avg `1.0479` n `12`; crypto_alt avg `-4.0443` n `233`; crypto_major avg `-3.1981` n `8`; equity avg `-2.2084` n `135`; fx avg `0.1145` n `6`; index avg `-0.3715` n `26`; metal avg `-1.3064` n `20`; unknown avg `-0.3976` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
