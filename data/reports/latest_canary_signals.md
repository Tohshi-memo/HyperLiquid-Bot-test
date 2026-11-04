# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T15:52:30.313847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.9881` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `2.2422` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.1222` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7213` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.2362` n `13`; crypto_alt avg `-0.3009` n `239`; crypto_major avg `-0.3751` n `8`; equity avg `-1.2345` n `158`; fx avg `-0.0115` n `6`; index avg `-0.1045` n `27`; metal avg `0.0357` n `20`; unknown avg `2.5904` n `1264`
- 1h: commodity avg `0.0627` n `13`; crypto_alt avg `0.6471` n `239`; crypto_major avg `0.7237` n `8`; equity avg `-1.5185` n `158`; fx avg `-0.0376` n `6`; index avg `-0.1129` n `27`; metal avg `0.0327` n `20`; unknown avg `161.1516` n `1256`
- 4h: commodity avg `-0.3378` n `13`; crypto_alt avg `1.3288` n `239`; crypto_major avg `1.7844` n `8`; equity avg `-2.2037` n `158`; fx avg `-0.0309` n `6`; index avg `-0.0844` n `27`; metal avg `0.0631` n `20`; unknown avg `4.3662` n `1252`
- 24h: commodity avg `-0.438` n `13`; crypto_alt avg `2.7477` n `239`; crypto_major avg `2.3329` n `8`; equity avg `-1.2205` n `158`; fx avg `0.0965` n `6`; index avg `0.0331` n `27`; metal avg `0.9017` n `20`; unknown avg `3.3291` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2618`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
