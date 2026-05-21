# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T13:37:21.314326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.21` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.5043` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.1697` n `12`; crypto_alt avg `-0.2338` n `228`; crypto_major avg `-0.1771` n `8`; equity avg `0.3038` n `66`; fx avg `-0.0158` n `6`; index avg `0.0139` n `23`; metal avg `-0.1601` n `18`; unknown avg `0.0125` n `386`
- 1h: commodity avg `0.7587` n `12`; crypto_alt avg `0.0639` n `228`; crypto_major avg `0.2516` n `8`; equity avg `0.2589` n `66`; fx avg `-0.0225` n `6`; index avg `-0.0119` n `23`; metal avg `-0.2403` n `18`; unknown avg `-0.2673` n `386`
- 4h: commodity avg `1.8869` n `12`; crypto_alt avg `-0.6242` n `228`; crypto_major avg `-0.6174` n `8`; equity avg `-0.3232` n `66`; fx avg `-0.0462` n `6`; index avg `-0.3979` n `23`; metal avg `-0.8609` n `18`; unknown avg `1.5737` n `386`
- 24h: commodity avg `-0.3601` n `12`; crypto_alt avg `2.2227` n `228`; crypto_major avg `2.5044` n `8`; equity avg `1.7426` n `66`; fx avg `0.0132` n `6`; index avg `0.8974` n `23`; metal avg `-0.0441` n `18`; unknown avg `6.1794` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
