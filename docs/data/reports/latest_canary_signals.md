# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T17:22:32.046426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6991` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.1244` n `12`; crypto_alt avg `0.3426` n `228`; crypto_major avg `0.3421` n `8`; equity avg `0.1368` n `66`; fx avg `-0.0002` n `6`; index avg `0.0797` n `23`; metal avg `0.0684` n `18`; unknown avg `-0.2727` n `384`
- 1h: commodity avg `-0.7019` n `12`; crypto_alt avg `0.5266` n `228`; crypto_major avg `0.5337` n `8`; equity avg `0.1201` n `66`; fx avg `-0.0123` n `6`; index avg `-0.0142` n `23`; metal avg `0.2292` n `18`; unknown avg `0.6533` n `384`
- 4h: commodity avg `-1.7715` n `12`; crypto_alt avg `1.5955` n `228`; crypto_major avg `0.9276` n `8`; equity avg `0.572` n `66`; fx avg `-0.0031` n `6`; index avg `0.751` n `23`; metal avg `0.9186` n `18`; unknown avg `0.6124` n `384`
- 24h: commodity avg `-2.835` n `12`; crypto_alt avg `2.4298` n `228`; crypto_major avg `1.5254` n `8`; equity avg `0.7555` n `66`; fx avg `-0.0273` n `6`; index avg `0.5982` n `23`; metal avg `0.8973` n `18`; unknown avg `1.292` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.042`, n `668`, weak_sample_signal
