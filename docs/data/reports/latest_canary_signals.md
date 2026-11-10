# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T19:22:27.826812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1359` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.5465` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5311` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0695` n `13`; crypto_alt avg `-0.3081` n `239`; crypto_major avg `-0.138` n `8`; equity avg `-0.2032` n `160`; fx avg `0.0044` n `6`; index avg `-0.0193` n `27`; metal avg `0.0083` n `20`; unknown avg `19.2375` n `1262`
- 1h: commodity avg `0.0538` n `13`; crypto_alt avg `-0.1984` n `239`; crypto_major avg `0.3892` n `8`; equity avg `0.3816` n `160`; fx avg `0.0163` n `6`; index avg `0.0518` n `27`; metal avg `0.0698` n `20`; unknown avg `-0.1421` n `1256`
- 4h: commodity avg `0.4107` n `13`; crypto_alt avg `-2.3654` n `239`; crypto_major avg `-1.7252` n `8`; equity avg `-1.9311` n `160`; fx avg `-0.021` n `6`; index avg `-0.1941` n `27`; metal avg `-0.1787` n `20`; unknown avg `-0.7223` n `1250`
- 24h: commodity avg `-0.2413` n `13`; crypto_alt avg `-2.0728` n `239`; crypto_major avg `-2.8481` n `8`; equity avg `-1.6937` n `160`; fx avg `-0.0868` n `6`; index avg `-0.1728` n `27`; metal avg `-0.4339` n `20`; unknown avg `-0.1495` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2483`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1809`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
