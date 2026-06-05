# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T10:22:25.506383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1751` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0951` n `12`; crypto_alt avg `-0.2868` n `228`; crypto_major avg `-0.127` n `8`; equity avg `0.084` n `74`; fx avg `0.0097` n `6`; index avg `0.0458` n `23`; metal avg `0.1241` n `18`; unknown avg `-0.0565` n `424`
- 1h: commodity avg `0.1288` n `12`; crypto_alt avg `0.1825` n `228`; crypto_major avg `-0.1161` n `8`; equity avg `0.159` n `74`; fx avg `0.002` n `6`; index avg `-0.0327` n `23`; metal avg `0.0935` n `18`; unknown avg `0.4314` n `424`
- 4h: commodity avg `-0.2247` n `12`; crypto_alt avg `1.6418` n `228`; crypto_major avg `1.9504` n `8`; equity avg `0.8024` n `74`; fx avg `0.0414` n `6`; index avg `0.1523` n `23`; metal avg `0.8767` n `18`; unknown avg `2.4584` n `424`
- 24h: commodity avg `-0.5964` n `12`; crypto_alt avg `-3.8952` n `228`; crypto_major avg `-2.6615` n `8`; equity avg `0.0194` n `73`; fx avg `0.1131` n `6`; index avg `-0.0021` n `23`; metal avg `-0.2924` n `18`; unknown avg `1.3022` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
