# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T18:22:29.930842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `12`; crypto_alt avg `0.0753` n `234`; crypto_major avg `0.1457` n `8`; equity avg `-0.015` n `142`; fx avg `-0.0021` n `6`; index avg `-0.0023` n `26`; metal avg `0.0159` n `20`; unknown avg `3.8409` n `969`
- 1h: commodity avg `0.0299` n `12`; crypto_alt avg `-0.616` n `234`; crypto_major avg `-0.3945` n `8`; equity avg `0.0159` n `142`; fx avg `0.0038` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.9076` n `967`
- 4h: commodity avg `0.0327` n `12`; crypto_alt avg `-0.1789` n `234`; crypto_major avg `0.4279` n `8`; equity avg `-0.3641` n `142`; fx avg `0.0282` n `6`; index avg `-0.1163` n `26`; metal avg `-0.1835` n `20`; unknown avg `3.3254` n `903`
- 24h: commodity avg `0.3237` n `12`; crypto_alt avg `0.6395` n `234`; crypto_major avg `0.8472` n `8`; equity avg `-0.1842` n `142`; fx avg `0.0651` n `6`; index avg `0.0576` n `26`; metal avg `-0.1801` n `20`; unknown avg `4.1266` n `820`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
