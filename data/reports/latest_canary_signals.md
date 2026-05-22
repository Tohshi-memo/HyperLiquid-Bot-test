# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T21:07:17.623939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2562` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4954` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1296` n `12`; crypto_alt avg `0.0329` n `228`; crypto_major avg `-0.0633` n `8`; equity avg `-0.005` n `67`; fx avg `0.0105` n `6`; index avg `-0.0008` n `23`; metal avg `0.039` n `18`; unknown avg `1.1009` n `386`
- 1h: commodity avg `0.3275` n `12`; crypto_alt avg `0.1045` n `228`; crypto_major avg `-0.1517` n `8`; equity avg `-0.0681` n `67`; fx avg `-0.0051` n `6`; index avg `-0.0523` n `23`; metal avg `0.0227` n `18`; unknown avg `1.0569` n `386`
- 4h: commodity avg `0.4313` n `12`; crypto_alt avg `-2.5437` n `228`; crypto_major avg `-1.8249` n `8`; equity avg `-1.036` n `67`; fx avg `0.0281` n `6`; index avg `-0.3295` n `23`; metal avg `-0.3475` n `18`; unknown avg `2.2851` n `386`
- 24h: commodity avg `-1.1093` n `12`; crypto_alt avg `-2.9284` n `228`; crypto_major avg `-2.3289` n `8`; equity avg `-1.1168` n `67`; fx avg `0.1512` n `6`; index avg `0.4759` n `23`; metal avg `-1.038` n `18`; unknown avg `-0.1222` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
