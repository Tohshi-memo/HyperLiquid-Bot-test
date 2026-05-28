# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T03:52:16.376703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2155` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.0043` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0573` n `12`; crypto_alt avg `-0.2693` n `228`; crypto_major avg `-0.379` n `8`; equity avg `-0.1612` n `67`; fx avg `-0.0206` n `6`; index avg `-0.028` n `23`; metal avg `-0.0445` n `18`; unknown avg `-0.4685` n `419`
- 1h: commodity avg `0.4929` n `12`; crypto_alt avg `-1.6501` n `228`; crypto_major avg `-1.3919` n `8`; equity avg `-1.1297` n `67`; fx avg `-0.0518` n `6`; index avg `-0.4015` n `23`; metal avg `-0.5545` n `18`; unknown avg `-0.1568` n `419`
- 4h: commodity avg `0.6793` n `12`; crypto_alt avg `-2.0931` n `228`; crypto_major avg `-1.5362` n `8`; equity avg `-1.442` n `67`; fx avg `-0.0411` n `6`; index avg `-0.5319` n `23`; metal avg `-1.5237` n `18`; unknown avg `-0.3931` n `419`
- 24h: commodity avg `0.2035` n `12`; crypto_alt avg `-3.5853` n `228`; crypto_major avg `-3.0289` n `8`; equity avg `-2.0736` n `67`; fx avg `-0.0826` n `6`; index avg `-1.2767` n `23`; metal avg `-2.7434` n `18`; unknown avg `-1.4693` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
