# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T18:22:23.968771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5738` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.6029` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0329` n `12`; crypto_alt avg `-0.2566` n `228`; crypto_major avg `-0.2755` n `8`; equity avg `0.0298` n `69`; fx avg `0.0022` n `6`; index avg `0.0606` n `23`; metal avg `0.0708` n `18`; unknown avg `-0.2592` n `419`
- 1h: commodity avg `-0.1547` n `12`; crypto_alt avg `-0.3515` n `228`; crypto_major avg `-0.5728` n `8`; equity avg `-0.1298` n `69`; fx avg `-0.0023` n `6`; index avg `-0.0665` n `23`; metal avg `0.0689` n `18`; unknown avg `-0.0182` n `419`
- 4h: commodity avg `-0.7659` n `12`; crypto_alt avg `2.2304` n `228`; crypto_major avg `1.8079` n `8`; equity avg `1.1134` n `69`; fx avg `0.0922` n `6`; index avg `0.117` n `23`; metal avg `0.205` n `18`; unknown avg `1.1559` n `418`
- 24h: commodity avg `-0.6191` n `12`; crypto_alt avg `0.6001` n `228`; crypto_major avg `0.9994` n `8`; equity avg `1.182` n `69`; fx avg `0.1937` n `6`; index avg `-0.1093` n `23`; metal avg `0.071` n `18`; unknown avg `0.9578` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1893`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
