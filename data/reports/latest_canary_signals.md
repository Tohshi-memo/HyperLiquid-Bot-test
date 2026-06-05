# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T19:07:29.704523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-2.8697` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `-2.7587` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.3729` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-2.1963` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `2.0234` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9192` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2683` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1775` n `12`; crypto_alt avg `-0.8729` n `228`; crypto_major avg `-0.2862` n `8`; equity avg `0.4101` n `74`; fx avg `-0.0076` n `6`; index avg `-0.0119` n `23`; metal avg `0.0155` n `18`; unknown avg `-0.3799` n `424`
- 1h: commodity avg `0.0616` n `12`; crypto_alt avg `-3.731` n `228`; crypto_major avg `-2.8081` n `8`; equity avg `-0.6118` n `74`; fx avg `-0.007` n `6`; index avg `-0.7847` n `23`; metal avg `-0.4352` n `18`; unknown avg `-1.1883` n `424`
- 4h: commodity avg `-0.5703` n `12`; crypto_alt avg `-3.943` n `228`; crypto_major avg `-3.329` n `8`; equity avg `-2.7729` n `74`; fx avg `-0.102` n `6`; index avg `-2.0607` n `23`; metal avg `-1.4098` n `18`; unknown avg `-1.4595` n `424`
- 24h: commodity avg `-1.6984` n `12`; crypto_alt avg `-10.9532` n `228`; crypto_major avg `-8.863` n `8`; equity avg `-6.8311` n `74`; fx avg `-0.0716` n `6`; index avg `-4.4054` n `23`; metal avg `-4.6364` n `18`; unknown avg `-2.3618` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
