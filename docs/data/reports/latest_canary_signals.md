# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T19:07:30.296928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `-0.0156` n `230`; crypto_major avg `-0.1019` n `8`; equity avg `-0.0607` n `113`; fx avg `0.0013` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0501` n `20`; unknown avg `-0.1308` n `785`
- 1h: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.0766` n `230`; crypto_major avg `-0.2183` n `8`; equity avg `-0.1236` n `113`; fx avg `0.006` n `6`; index avg `-0.0268` n `25`; metal avg `0.0011` n `20`; unknown avg `-0.0928` n `785`
- 4h: commodity avg `0.1628` n `12`; crypto_alt avg `-0.5003` n `230`; crypto_major avg `-0.0798` n `8`; equity avg `-0.3226` n `113`; fx avg `0.0157` n `6`; index avg `-0.1239` n `25`; metal avg `-0.1881` n `20`; unknown avg `-0.1453` n `785`
- 24h: commodity avg `0.1972` n `12`; crypto_alt avg `-1.8844` n `230`; crypto_major avg `-0.2988` n `8`; equity avg `0.0317` n `113`; fx avg `-0.0514` n `6`; index avg `0.0115` n `25`; metal avg `-0.2504` n `20`; unknown avg `-0.2945` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2011`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1998`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1935`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
