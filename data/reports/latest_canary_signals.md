# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T18:07:42.262096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6081` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.458` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.4307` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.2001` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0182` n `12`; crypto_alt avg `-0.3155` n `234`; crypto_major avg `-0.2488` n `8`; equity avg `-0.0542` n `141`; fx avg `0.005` n `6`; index avg `-0.0042` n `26`; metal avg `0.0244` n `20`; unknown avg `1.9621` n `941`
- 1h: commodity avg `0.0027` n `12`; crypto_alt avg `0.441` n `234`; crypto_major avg `0.5139` n `8`; equity avg `0.3179` n `141`; fx avg `0.0082` n `6`; index avg `0.0601` n `26`; metal avg `0.1014` n `20`; unknown avg `2.9892` n `933`
- 4h: commodity avg `0.0953` n `12`; crypto_alt avg `-3.222` n `234`; crypto_major avg `-2.5128` n `8`; equity avg `-0.3127` n `141`; fx avg `-0.0288` n `6`; index avg `-0.0821` n `26`; metal avg `-0.0548` n `20`; unknown avg `3.7729` n `919`
- 24h: commodity avg `0.5453` n `12`; crypto_alt avg `-2.6442` n `234`; crypto_major avg `-3.3584` n `8`; equity avg `-1.2422` n `140`; fx avg `0.0112` n `6`; index avg `-0.3436` n `26`; metal avg `-0.7345` n `20`; unknown avg `12.7848` n `878`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
