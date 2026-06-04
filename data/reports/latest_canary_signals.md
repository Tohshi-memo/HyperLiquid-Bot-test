# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T07:22:25.241109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0875` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0315` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.9228` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.8602` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.821` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `-1.7748` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-1.6867` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0352` n `12`; crypto_alt avg `-0.5334` n `228`; crypto_major avg `-0.393` n `8`; equity avg `-0.1968` n `73`; fx avg `0.0372` n `6`; index avg `-0.0464` n `23`; metal avg `-0.0309` n `18`; unknown avg `0.7975` n `424`
- 1h: commodity avg `-0.1006` n `12`; crypto_alt avg `-1.7413` n `228`; crypto_major avg `-1.8473` n `8`; equity avg `-0.1606` n `73`; fx avg `0.0703` n `6`; index avg `0.0129` n `23`; metal avg `-0.0263` n `18`; unknown avg `0.3443` n `424`
- 4h: commodity avg `0.099` n `12`; crypto_alt avg `-2.4085` n `228`; crypto_major avg `-1.9885` n `8`; equity avg `-0.0657` n `73`; fx avg `0.0828` n `6`; index avg `0.043` n `23`; metal avg `-0.2137` n `18`; unknown avg `0.6296` n `404`
- 24h: commodity avg `-0.336` n `12`; crypto_alt avg `-5.7667` n `228`; crypto_major avg `-5.1618` n `8`; equity avg `-3.8626` n `73`; fx avg `0.0004` n `6`; index avg `-1.1039` n `23`; metal avg `-1.2998` n `18`; unknown avg `0.1512` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
