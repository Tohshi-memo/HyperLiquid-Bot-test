# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T05:22:16.479091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2` n `12`; crypto_alt avg `-0.5503` n `228`; crypto_major avg `-0.3335` n `8`; equity avg `-0.0874` n `66`; fx avg `0.0041` n `6`; index avg `0.0131` n `23`; metal avg `-0.1399` n `18`; unknown avg `-0.288` n `383`
- 1h: commodity avg `0.1484` n `12`; crypto_alt avg `-0.4423` n `228`; crypto_major avg `-0.3023` n `8`; equity avg `-0.1231` n `66`; fx avg `0.0046` n `6`; index avg `0.0865` n `23`; metal avg `-0.0799` n `18`; unknown avg `-0.3402` n `383`
- 4h: commodity avg `0.052` n `12`; crypto_alt avg `-0.2856` n `228`; crypto_major avg `-0.355` n `8`; equity avg `-0.0173` n `66`; fx avg `0.0459` n `6`; index avg `-0.078` n `23`; metal avg `-0.704` n `18`; unknown avg `-0.8074` n `383`
- 24h: commodity avg `0.2449` n `12`; crypto_alt avg `0.4607` n `228`; crypto_major avg `-0.0319` n `8`; equity avg `-0.9512` n `66`; fx avg `0.2715` n `6`; index avg `-0.3125` n `23`; metal avg `0.1903` n `18`; unknown avg `0.5138` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
