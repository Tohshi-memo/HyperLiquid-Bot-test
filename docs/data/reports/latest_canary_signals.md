# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T21:37:13.397774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2726` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.2078` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `0.0806` n `228`; crypto_major avg `0.1271` n `8`; equity avg `-0.0003` n `67`; fx avg `-0.009` n `6`; index avg `0.0009` n `23`; metal avg `0.0043` n `18`; unknown avg `-0.0098` n `386`
- 1h: commodity avg `0.2619` n `12`; crypto_alt avg `0.6516` n `228`; crypto_major avg `0.4381` n `8`; equity avg `-0.0492` n `67`; fx avg `-0.0057` n `6`; index avg `-0.0213` n `23`; metal avg `-0.02` n `18`; unknown avg `0.0855` n `386`
- 4h: commodity avg `0.6826` n `12`; crypto_alt avg `-2.4783` n `228`; crypto_major avg `-1.59` n `8`; equity avg `-1.112` n `67`; fx avg `0.0287` n `6`; index avg `-0.3822` n `23`; metal avg `-0.3223` n `18`; unknown avg `1.6689` n `386`
- 24h: commodity avg `-0.8564` n `12`; crypto_alt avg `-2.8145` n `228`; crypto_major avg `-1.9807` n `8`; equity avg `-1.0855` n `67`; fx avg `0.1835` n `6`; index avg `0.5151` n `23`; metal avg `-1.0322` n `18`; unknown avg `-1.2881` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
