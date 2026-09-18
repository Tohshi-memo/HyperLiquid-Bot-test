# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T15:52:31.784542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.6746` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.589` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.1182` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.136` n `234`; crypto_major avg `-0.0957` n `8`; equity avg `0.0371` n `140`; fx avg `0.0076` n `6`; index avg `-0.0117` n `26`; metal avg `0.0155` n `20`; unknown avg `-0.052` n `928`
- 1h: commodity avg `0.0821` n `12`; crypto_alt avg `0.0356` n `234`; crypto_major avg `-0.5175` n `8`; equity avg `-0.0165` n `140`; fx avg `0.0105` n `6`; index avg `-0.0296` n `26`; metal avg `-0.0134` n `20`; unknown avg `-0.0324` n `914`
- 4h: commodity avg `0.3502` n `12`; crypto_alt avg `1.5425` n `234`; crypto_major avg `2.4684` n `8`; equity avg `-0.1206` n `140`; fx avg `-0.0306` n `6`; index avg `-0.1246` n `26`; metal avg `-0.2062` n `20`; unknown avg `1.1739` n `884`
- 24h: commodity avg `0.1913` n `12`; crypto_alt avg `6.0683` n `234`; crypto_major avg `5.7755` n `8`; equity avg `0.6129` n `140`; fx avg `0.2271` n `6`; index avg `-0.1276` n `26`; metal avg `0.0955` n `20`; unknown avg `2.0147` n `717`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
