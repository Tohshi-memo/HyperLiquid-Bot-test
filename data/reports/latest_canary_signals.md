# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T03:52:26.965804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0609` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4991` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0047` n `12`; crypto_alt avg `-0.3274` n `228`; crypto_major avg `-0.2339` n `8`; equity avg `-0.1941` n `74`; fx avg `0.0025` n `6`; index avg `-0.0823` n `23`; metal avg `-0.0566` n `18`; unknown avg `-0.1371` n `424`
- 1h: commodity avg `-0.1493` n `12`; crypto_alt avg `-0.601` n `228`; crypto_major avg `-0.5922` n `8`; equity avg `-0.4337` n `74`; fx avg `0.0218` n `6`; index avg `-0.1561` n `23`; metal avg `-0.2182` n `18`; unknown avg `0.6114` n `424`
- 4h: commodity avg `0.0013` n `12`; crypto_alt avg `-2.6989` n `228`; crypto_major avg `-2.0596` n `8`; equity avg `-0.8016` n `74`; fx avg `0.1321` n `6`; index avg `-0.5605` n `23`; metal avg `-0.8585` n `18`; unknown avg `1.1716` n `424`
- 24h: commodity avg `-0.2004` n `12`; crypto_alt avg `-6.7597` n `228`; crypto_major avg `-5.4773` n `8`; equity avg `-1.67` n `73`; fx avg `0.2035` n `6`; index avg `-0.6164` n `23`; metal avg `-0.481` n `18`; unknown avg `-0.6976` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
