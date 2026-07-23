# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T11:37:31.126525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0447` n `12`; crypto_alt avg `-0.1071` n `230`; crypto_major avg `-0.1168` n `8`; equity avg `-0.3308` n `99`; fx avg `-0.0116` n `6`; index avg `-0.0677` n `25`; metal avg `-0.0485` n `20`; unknown avg `-0.0051` n `772`
- 1h: commodity avg `0.0444` n `12`; crypto_alt avg `-0.0646` n `230`; crypto_major avg `-0.1038` n `8`; equity avg `-0.6268` n `99`; fx avg `-0.0166` n `6`; index avg `-0.1245` n `25`; metal avg `-0.0948` n `20`; unknown avg `-0.0289` n `772`
- 4h: commodity avg `0.1477` n `12`; crypto_alt avg `0.2199` n `230`; crypto_major avg `0.4553` n `8`; equity avg `0.022` n `99`; fx avg `-0.0684` n `6`; index avg `-0.0069` n `25`; metal avg `-0.0848` n `20`; unknown avg `0.0665` n `772`
- 24h: commodity avg `0.8344` n `12`; crypto_alt avg `-0.3031` n `230`; crypto_major avg `-0.0973` n `8`; equity avg `0.2945` n `99`; fx avg `-0.1055` n `6`; index avg `0.096` n `25`; metal avg `-0.4627` n `20`; unknown avg `10.0044` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0766`, n `666`, weak_sample_signal
