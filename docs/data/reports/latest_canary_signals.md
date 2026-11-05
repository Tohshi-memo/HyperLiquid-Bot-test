# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T03:37:25.189080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0375` n `13`; crypto_alt avg `0.0818` n `239`; crypto_major avg `0.0452` n `8`; equity avg `0.0064` n `158`; fx avg `0.0044` n `6`; index avg `-0.0202` n `27`; metal avg `-0.0143` n `20`; unknown avg `-0.4503` n `1263`
- 1h: commodity avg `-0.1574` n `13`; crypto_alt avg `0.5615` n `239`; crypto_major avg `0.3034` n `8`; equity avg `-0.1876` n `158`; fx avg `0.0023` n `6`; index avg `-0.0558` n `27`; metal avg `0.0914` n `20`; unknown avg `-0.4337` n `1257`
- 4h: commodity avg `-0.302` n `13`; crypto_alt avg `0.7142` n `239`; crypto_major avg `0.3501` n `8`; equity avg `-0.5847` n `158`; fx avg `0.043` n `6`; index avg `-0.1908` n `27`; metal avg `0.492` n `20`; unknown avg `3.7167` n `1248`
- 24h: commodity avg `-1.7608` n `13`; crypto_alt avg `4.7442` n `239`; crypto_major avg `4.6872` n `8`; equity avg `1.2506` n `158`; fx avg `0.1568` n `6`; index avg `0.4968` n `27`; metal avg `2.0124` n `20`; unknown avg `33.3878` n `1032`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2512`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1983`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
