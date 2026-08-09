# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T16:37:29.792200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0362` n `12`; crypto_alt avg `0.0858` n `230`; crypto_major avg `0.0395` n `8`; equity avg `0.0263` n `112`; fx avg `0.0034` n `6`; index avg `0.0004` n `25`; metal avg `0.0021` n `20`; unknown avg `0.0125` n `785`
- 1h: commodity avg `-0.056` n `12`; crypto_alt avg `0.3203` n `230`; crypto_major avg `0.0299` n `8`; equity avg `0.0301` n `112`; fx avg `0.0107` n `6`; index avg `0.0058` n `25`; metal avg `0.0022` n `20`; unknown avg `0.0159` n `785`
- 4h: commodity avg `-0.0753` n `10`; crypto_alt avg `0.9273` n `228`; crypto_major avg `0.78` n `7`; equity avg `0.136` n `108`; fx avg `0.0017` n `6`; index avg `0.0265` n `24`; metal avg `0.0777` n `13`; unknown avg `0.0377` n `769`
- 24h: commodity avg `0.1082` n `12`; crypto_alt avg `1.0815` n `230`; crypto_major avg `0.2253` n `8`; equity avg `0.3383` n `112`; fx avg `0.0066` n `6`; index avg `0.0353` n `25`; metal avg `0.0883` n `20`; unknown avg `0.4146` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
