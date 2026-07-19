# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T08:22:22.223865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `-0.0807` n `230`; crypto_major avg `-0.0611` n `8`; equity avg `0.0244` n `96`; fx avg `-0.0028` n `6`; index avg `0.0076` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.0041` n `770`
- 1h: commodity avg `0.033` n `12`; crypto_alt avg `-0.0394` n `230`; crypto_major avg `0.0212` n `8`; equity avg `0.1388` n `96`; fx avg `0.0079` n `6`; index avg `0.0008` n `25`; metal avg `-0.0159` n `20`; unknown avg `-0.0021` n `770`
- 4h: commodity avg `0.0363` n `12`; crypto_alt avg `0.1094` n `230`; crypto_major avg `0.1702` n `8`; equity avg `0.1908` n `96`; fx avg `0.0211` n `6`; index avg `0.0249` n `25`; metal avg `-0.0062` n `20`; unknown avg `0.0395` n `752`
- 24h: commodity avg `0.3176` n `12`; crypto_alt avg `0.2201` n `230`; crypto_major avg `0.9172` n `8`; equity avg `0.2207` n `96`; fx avg `-0.0003` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0502` n `20`; unknown avg `0.0355` n `751`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
