# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T11:22:18.073151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.1431` n `228`; crypto_major avg `-0.1869` n `8`; equity avg `-0.1184` n `66`; fx avg `-0.0061` n `6`; index avg `-0.0299` n `23`; metal avg `-0.0618` n `18`; unknown avg `-0.3262` n `383`
- 1h: commodity avg `0.2316` n `12`; crypto_alt avg `-0.1942` n `228`; crypto_major avg `0.0534` n `8`; equity avg `0.0266` n `66`; fx avg `-0.0466` n `6`; index avg `0.0488` n `23`; metal avg `0.107` n `18`; unknown avg `-0.2162` n `383`
- 4h: commodity avg `0.1194` n `12`; crypto_alt avg `-1.0338` n `228`; crypto_major avg `-0.6253` n `8`; equity avg `-0.7906` n `66`; fx avg `-0.0623` n `6`; index avg `-0.4106` n `23`; metal avg `-0.1095` n `18`; unknown avg `-0.8066` n `383`
- 24h: commodity avg `0.6982` n `12`; crypto_alt avg `1.1572` n `228`; crypto_major avg `0.8237` n `8`; equity avg `-1.4075` n `66`; fx avg `0.195` n `6`; index avg `-0.5946` n `23`; metal avg `0.0431` n `18`; unknown avg `0.7171` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
