# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T18:37:32.569293+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0126` n `12`; crypto_alt avg `-0.4752` n `234`; crypto_major avg `-0.3122` n `8`; equity avg `-0.0772` n `142`; fx avg `-0.0082` n `6`; index avg `-0.0165` n `26`; metal avg `0.0314` n `20`; unknown avg `2.9227` n `969`
- 1h: commodity avg `0.0549` n `12`; crypto_alt avg `-0.6205` n `234`; crypto_major avg `-0.2525` n `8`; equity avg `0.013` n `142`; fx avg `-0.0117` n `6`; index avg `-0.0065` n `26`; metal avg `0.0328` n `20`; unknown avg `1.6899` n `967`
- 4h: commodity avg `0.0473` n `12`; crypto_alt avg `-0.4754` n `234`; crypto_major avg `0.3095` n `8`; equity avg `-0.1424` n `142`; fx avg `-0.0171` n `6`; index avg `-0.0731` n `26`; metal avg `-0.0256` n `20`; unknown avg `4.2197` n `903`
- 24h: commodity avg `0.3653` n `12`; crypto_alt avg `0.0734` n `234`; crypto_major avg `0.4058` n `8`; equity avg `-0.2372` n `142`; fx avg `0.0489` n `6`; index avg `0.0472` n `26`; metal avg `-0.1846` n `20`; unknown avg `5.8704` n `820`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
