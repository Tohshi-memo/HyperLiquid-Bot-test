# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T05:22:25.486245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0231` n `12`; crypto_alt avg `0.0706` n `230`; crypto_major avg `0.1472` n `8`; equity avg `-0.154` n `113`; fx avg `-0.0159` n `6`; index avg `-0.0249` n `25`; metal avg `-0.0579` n `20`; unknown avg `0.1037` n `786`
- 1h: commodity avg `-0.009` n `12`; crypto_alt avg `-0.0344` n `230`; crypto_major avg `0.0247` n `8`; equity avg `-0.216` n `113`; fx avg `-0.0157` n `6`; index avg `-0.0507` n `25`; metal avg `-0.0314` n `20`; unknown avg `-0.188` n `786`
- 4h: commodity avg `0.0308` n `12`; crypto_alt avg `0.053` n `230`; crypto_major avg `0.0362` n `8`; equity avg `0.4597` n `113`; fx avg `0.0128` n `6`; index avg `0.0768` n `25`; metal avg `0.0312` n `20`; unknown avg `-0.2393` n `786`
- 24h: commodity avg `0.2237` n `12`; crypto_alt avg `-0.8781` n `230`; crypto_major avg `0.8587` n `8`; equity avg `1.5505` n `113`; fx avg `0.0031` n `6`; index avg `0.0938` n `25`; metal avg `-0.0484` n `20`; unknown avg `-0.0492` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2226`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2194`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2129`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1996`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
