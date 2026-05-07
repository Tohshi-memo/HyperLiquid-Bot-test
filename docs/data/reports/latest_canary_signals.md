# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T07:37:16.660371+00:00`
- Correlation status: `ready`
- Asset price records: `530`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.27` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.1346` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.2088` n `12`; crypto_alt avg `0.1647` n `228`; crypto_major avg `0.2795` n `8`; equity avg `0.0221` n `65`; fx avg `0.0351` n `4`; index avg `0.0238` n `23`; metal avg `0.0731` n `18`; unknown avg `-0.2441` n `358`
- 1h: commodity avg `-0.8721` n `12`; crypto_alt avg `0.6521` n `228`; crypto_major avg `0.5351` n `8`; equity avg `0.356` n `65`; fx avg `-0.058` n `4`; index avg `0.0987` n `23`; metal avg `0.3933` n `18`; unknown avg `0.1299` n `358`
- 4h: commodity avg `-0.9216` n `12`; crypto_alt avg `2.045` n `228`; crypto_major avg `1.213` n `8`; equity avg `0.7902` n `65`; fx avg `-0.0547` n `4`; index avg `0.2429` n `23`; metal avg `1.0338` n `18`; unknown avg `0.5946` n `356`
- 24h: commodity avg `-2.5761` n `7`; crypto_alt avg `1.4063` n `223`; crypto_major avg `-0.4585` n `7`; equity avg `1.9757` n `47`; fx avg `-0.115` n `4`; index avg `1.5594` n `6`; metal avg `2.4037` n `7`; unknown avg `0.9103` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1295`, n `526`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.12`, n `526`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1001`, n `522`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0897`, n `522`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0864`, n `526`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `522`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0807`, n `522`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0752`, n `522`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `522`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0647`, n `526`, weak_sample_signal
