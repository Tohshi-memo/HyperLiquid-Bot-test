# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T11:22:28.425251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0353` n `12`; crypto_alt avg `0.1576` n `234`; crypto_major avg `0.0965` n `8`; equity avg `-0.0193` n `142`; fx avg `0.0067` n `6`; index avg `-0.01` n `26`; metal avg `-0.0402` n `20`; unknown avg `0.9115` n `963`
- 1h: commodity avg `0.0135` n `12`; crypto_alt avg `-0.0159` n `234`; crypto_major avg `0.1365` n `8`; equity avg `-0.1538` n `142`; fx avg `0.0117` n `6`; index avg `-0.0467` n `26`; metal avg `-0.1038` n `20`; unknown avg `1.8266` n `961`
- 4h: commodity avg `0.4066` n `12`; crypto_alt avg `0.8739` n `234`; crypto_major avg `0.8667` n `8`; equity avg `-0.3533` n `142`; fx avg `0.0835` n `6`; index avg `-0.1197` n `26`; metal avg `-0.2493` n `20`; unknown avg `2.1234` n `945`
- 24h: commodity avg `-0.2181` n `12`; crypto_alt avg `-0.0466` n `234`; crypto_major avg `-0.2466` n `8`; equity avg `-0.2438` n `142`; fx avg `0.0514` n `6`; index avg `-0.0498` n `26`; metal avg `-0.0255` n `20`; unknown avg `2682.7957` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
