# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T04:22:23.879873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0278` n `12`; crypto_alt avg `0.2487` n `230`; crypto_major avg `0.192` n `8`; equity avg `0.1986` n `98`; fx avg `0.0079` n `6`; index avg `0.0472` n `25`; metal avg `0.043` n `20`; unknown avg `0.0226` n `773`
- 1h: commodity avg `-0.0653` n `12`; crypto_alt avg `0.2216` n `230`; crypto_major avg `0.1169` n `8`; equity avg `0.2626` n `98`; fx avg `-0.0106` n `6`; index avg `0.0843` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.1232` n `773`
- 4h: commodity avg `0.1078` n `12`; crypto_alt avg `-0.4722` n `230`; crypto_major avg `-0.6016` n `8`; equity avg `-0.3178` n `98`; fx avg `-0.0737` n `6`; index avg `-0.0352` n `25`; metal avg `0.1334` n `20`; unknown avg `0.4603` n `773`
- 24h: commodity avg `0.7343` n `12`; crypto_alt avg `-0.6811` n `230`; crypto_major avg `-0.7878` n `8`; equity avg `-0.6024` n `98`; fx avg `-0.167` n `6`; index avg `-0.0799` n `25`; metal avg `-0.0151` n `20`; unknown avg `1.8546` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.087`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
