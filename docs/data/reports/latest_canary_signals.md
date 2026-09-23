# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T16:07:40.418289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.516` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.1965` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0581` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8662` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0369` n `12`; crypto_alt avg `0.3299` n `234`; crypto_major avg `0.4237` n `8`; equity avg `0.0957` n `141`; fx avg `-0.006` n `6`; index avg `0.0044` n `26`; metal avg `0.0373` n `20`; unknown avg `0.1533` n `929`
- 1h: commodity avg `0.1946` n `12`; crypto_alt avg `-1.3855` n `234`; crypto_major avg `-0.7581` n `8`; equity avg `-0.2215` n `141`; fx avg `-0.0056` n `6`; index avg `-0.0514` n `26`; metal avg `-0.1051` n `20`; unknown avg `0.0697` n `927`
- 4h: commodity avg `0.148` n `12`; crypto_alt avg `-3.7731` n `234`; crypto_major avg `-2.368` n `8`; equity avg `-0.5018` n `141`; fx avg `-0.0153` n `6`; index avg `-0.1715` n `26`; metal avg `-0.3099` n `20`; unknown avg `514.0272` n `891`
- 24h: commodity avg `0.3547` n `12`; crypto_alt avg `-1.9112` n `234`; crypto_major avg `-2.8248` n `8`; equity avg `-0.7809` n `140`; fx avg `0.0058` n `6`; index avg `-0.2526` n `26`; metal avg `-0.5055` n `20`; unknown avg `15.371` n `838`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2519`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
