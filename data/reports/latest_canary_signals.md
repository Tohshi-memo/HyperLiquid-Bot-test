# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T04:52:21.584016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2499` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0757` n `12`; crypto_alt avg `-0.124` n `228`; crypto_major avg `-0.0106` n `8`; equity avg `-0.013` n `67`; fx avg `-0.0002` n `6`; index avg `-0.001` n `23`; metal avg `-0.0231` n `18`; unknown avg `-0.1487` n `419`
- 1h: commodity avg `-0.0283` n `12`; crypto_alt avg `-0.722` n `228`; crypto_major avg `-0.0535` n `8`; equity avg `-0.225` n `67`; fx avg `-0.0469` n `6`; index avg `-0.2131` n `23`; metal avg `-0.2833` n `18`; unknown avg `-0.5902` n `419`
- 4h: commodity avg `0.5762` n `12`; crypto_alt avg `-2.794` n `228`; crypto_major avg `-1.6737` n `8`; equity avg `-1.7736` n `67`; fx avg `-0.0957` n `6`; index avg `-0.7913` n `23`; metal avg `-2.0383` n `18`; unknown avg `-0.3575` n `419`
- 24h: commodity avg `0.3005` n `12`; crypto_alt avg `-4.1614` n `228`; crypto_major avg `-3.1882` n `8`; equity avg `-2.2031` n `67`; fx avg `-0.1216` n `6`; index avg `-1.4059` n `23`; metal avg `-3.2321` n `18`; unknown avg `-1.3978` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1876`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
