# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T03:07:22.268496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.4584` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.055` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.7629` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.5651` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.0018` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0351` n `12`; crypto_alt avg `1.1366` n `228`; crypto_major avg `0.8187` n `8`; equity avg `0.2431` n `73`; fx avg `0.007` n `6`; index avg `0.09` n `23`; metal avg `0.1455` n `18`; unknown avg `0.0052` n `420`
- 1h: commodity avg `-0.0375` n `12`; crypto_alt avg `2.8254` n `228`; crypto_major avg `2.4209` n `8`; equity avg `0.658` n `73`; fx avg `-0.0195` n `6`; index avg `0.1266` n `23`; metal avg `0.3659` n `18`; unknown avg `0.6418` n `420`
- 4h: commodity avg `-0.3422` n `12`; crypto_alt avg `-2.6277` n `228`; crypto_major avg `-1.0088` n `8`; equity avg `0.4376` n `73`; fx avg `-0.0385` n `6`; index avg `-0.007` n `23`; metal avg `0.5563` n `18`; unknown avg `-0.9425` n `419`
- 24h: commodity avg `-0.0035` n `12`; crypto_alt avg `-1.658` n `228`; crypto_major avg `-2.1123` n `8`; equity avg `-3.3866` n `73`; fx avg `-0.0146` n `6`; index avg `-1.1413` n `23`; metal avg `-1.5572` n `18`; unknown avg `0.2175` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
