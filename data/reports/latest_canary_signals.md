# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T16:52:14.170332+00:00`
- Correlation status: `ready`
- Asset price records: `567`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.9821` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.2909` n `12`; crypto_alt avg `0.1163` n `228`; crypto_major avg `0.0103` n `8`; equity avg `-0.0778` n `65`; fx avg `0.0126` n `5`; index avg `-0.1493` n `23`; metal avg `-0.1068` n `18`; unknown avg `0.846` n `365`
- 1h: commodity avg `0.9561` n `12`; crypto_alt avg `0.3334` n `228`; crypto_major avg `-0.1102` n `8`; equity avg `-0.7025` n `65`; fx avg `0.03` n `5`; index avg `-0.444` n `23`; metal avg `-0.4204` n `18`; unknown avg `0.7839` n `365`
- 4h: commodity avg `2.3894` n `12`; crypto_alt avg `-1.07` n `228`; crypto_major avg `-1.5927` n `8`; equity avg `-1.4092` n `65`; fx avg `0.0897` n `5`; index avg `-0.7835` n `23`; metal avg `-1.3773` n `18`; unknown avg `0.297` n `365`
- 24h: commodity avg `0.2344` n `12`; crypto_alt avg `0.1387` n `228`; crypto_major avg `-2.2407` n `8`; equity avg `-0.3056` n `65`; fx avg `0.1432` n `5`; index avg `-0.2707` n `23`; metal avg `0.7643` n `18`; unknown avg `0.5448` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1345`, n `563`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1179`, n `563`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `563`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1089`, n `563`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0994`, n `559`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.094`, n `559`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `559`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `559`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0823`, n `559`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `563`, weak_sample_signal
