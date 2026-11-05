# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T21:37:32.030580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0417` n `13`; crypto_alt avg `0.4888` n `239`; crypto_major avg `0.459` n `8`; equity avg `0.7862` n `158`; fx avg `-0.0076` n `6`; index avg `0.0293` n `27`; metal avg `0.0067` n `20`; unknown avg `0.732` n `1256`
- 1h: commodity avg `0.0916` n `13`; crypto_alt avg `-0.3628` n `239`; crypto_major avg `-0.1865` n `8`; equity avg `0.1013` n `158`; fx avg `-0.0259` n `6`; index avg `-0.1141` n `27`; metal avg `-0.081` n `20`; unknown avg `22.8508` n `1216`
- 4h: commodity avg `0.1593` n `13`; crypto_alt avg `0.8368` n `239`; crypto_major avg `-0.0799` n `8`; equity avg `-0.1547` n `158`; fx avg `-0.0316` n `6`; index avg `-0.2699` n `27`; metal avg `-0.219` n `20`; unknown avg `3.528` n `1194`
- 24h: commodity avg `0.8735` n `13`; crypto_alt avg `-4.3039` n `239`; crypto_major avg `-4.7938` n `8`; equity avg `-8.12` n `158`; fx avg `0.0704` n `6`; index avg `-1.3056` n `27`; metal avg `0.0691` n `20`; unknown avg `228.1835` n `1062`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
