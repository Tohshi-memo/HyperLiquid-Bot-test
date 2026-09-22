# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T03:07:31.306468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.121` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-1.9772` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8771` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7182` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0358` n `12`; crypto_alt avg `-0.2332` n `234`; crypto_major avg `-0.2604` n `8`; equity avg `-0.0619` n `140`; fx avg `-0.0036` n `6`; index avg `-0.0045` n `26`; metal avg `-0.0354` n `20`; unknown avg `-0.0847` n `942`
- 1h: commodity avg `0.0375` n `12`; crypto_alt avg `-0.3995` n `234`; crypto_major avg `-0.5059` n `8`; equity avg `0.0327` n `140`; fx avg `0.015` n `6`; index avg `-0.013` n `26`; metal avg `-0.0565` n `20`; unknown avg `0.3517` n `942`
- 4h: commodity avg `0.2362` n `12`; crypto_alt avg `-0.7135` n `234`; crypto_major avg `-1.8848` n `8`; equity avg `0.0924` n `140`; fx avg `-0.1493` n `6`; index avg `-0.0077` n `26`; metal avg `-0.1666` n `20`; unknown avg `1.1162` n `936`
- 24h: commodity avg `-0.1303` n `12`; crypto_alt avg `3.2503` n `234`; crypto_major avg `3.953` n `8`; equity avg `2.3843` n `140`; fx avg `-0.1929` n `6`; index avg `0.4759` n `26`; metal avg `-0.035` n `20`; unknown avg `8.5132` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
