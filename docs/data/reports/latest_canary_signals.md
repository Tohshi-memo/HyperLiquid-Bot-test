# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T13:22:26.136212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5603` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.2003` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0423` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7237` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.643` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `0.5679` n `230`; crypto_major avg `0.7056` n `8`; equity avg `0.0196` n `92`; fx avg `-0.0076` n `6`; index avg `-0.006` n `25`; metal avg `0.0447` n `20`; unknown avg `12.9077` n `766`
- 1h: commodity avg `-0.0151` n `12`; crypto_alt avg `1.6728` n `230`; crypto_major avg `2.1852` n `8`; equity avg `1.0855` n `92`; fx avg `-0.0289` n `6`; index avg `0.191` n `25`; metal avg `0.5422` n `20`; unknown avg `0.7458` n `766`
- 4h: commodity avg `-0.119` n `12`; crypto_alt avg `1.6887` n `230`; crypto_major avg `2.4413` n `8`; equity avg `0.7176` n `92`; fx avg `-0.018` n `6`; index avg `0.2362` n `25`; metal avg `0.399` n `20`; unknown avg `0.9954` n `766`
- 24h: commodity avg `1.4045` n `12`; crypto_alt avg `1.2926` n `230`; crypto_major avg `2.6654` n `8`; equity avg `0.3925` n `92`; fx avg `-0.0316` n `6`; index avg `0.1104` n `25`; metal avg `0.2405` n `20`; unknown avg `-0.0458` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
