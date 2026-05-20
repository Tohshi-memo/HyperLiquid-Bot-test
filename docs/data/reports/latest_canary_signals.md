# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T16:23:42.074381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1184` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.251` n `12`; crypto_alt avg `-0.3807` n `228`; crypto_major avg `-0.3653` n `8`; equity avg `-0.2026` n `66`; fx avg `0.0076` n `6`; index avg `0.0013` n `23`; metal avg `-0.1963` n `18`; unknown avg `-0.1798` n `384`
- 1h: commodity avg `0.1287` n `12`; crypto_alt avg `-0.1533` n `228`; crypto_major avg `-0.4094` n `8`; equity avg `-0.192` n `66`; fx avg `0.0306` n `6`; index avg `0.0258` n `23`; metal avg `-0.3522` n `18`; unknown avg `-0.0193` n `384`
- 4h: commodity avg `-1.2915` n `12`; crypto_alt avg `1.435` n `228`; crypto_major avg `0.8269` n `8`; equity avg `0.4875` n `66`; fx avg `0.0034` n `6`; index avg `0.7409` n `23`; metal avg `0.5742` n `18`; unknown avg `0.4575` n `384`
- 24h: commodity avg `-2.0107` n `12`; crypto_alt avg `2.6748` n `228`; crypto_major avg `1.6835` n `8`; equity avg `1.9959` n `66`; fx avg `0.0225` n `6`; index avg `1.3029` n `23`; metal avg `1.0528` n `18`; unknown avg `1.1038` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
