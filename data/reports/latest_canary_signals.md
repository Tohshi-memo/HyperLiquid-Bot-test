# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T11:58:41.804468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5499` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1752` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5017` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0445` n `12`; crypto_alt avg `-0.0412` n `229`; crypto_major avg `0.0763` n `8`; equity avg `0.1464` n `88`; fx avg `-0.0178` n `6`; index avg `0.046` n `25`; metal avg `-0.0071` n `20`; unknown avg `-0.0476` n `763`
- 1h: commodity avg `-0.1439` n `12`; crypto_alt avg `0.1317` n `229`; crypto_major avg `0.4185` n `8`; equity avg `0.3175` n `88`; fx avg `-0.0296` n `6`; index avg `0.0621` n `25`; metal avg `0.0253` n `20`; unknown avg `-0.2335` n `763`
- 4h: commodity avg `-0.2473` n `12`; crypto_alt avg `1.2491` n `228`; crypto_major avg `2.3026` n `8`; equity avg `0.8009` n `88`; fx avg `-0.036` n `6`; index avg `0.0853` n `25`; metal avg `0.1274` n `20`; unknown avg `0.4742` n `763`
- 24h: commodity avg `-0.6155` n `12`; crypto_alt avg `3.1213` n `228`; crypto_major avg `4.4665` n `8`; equity avg `-1.6307` n `88`; fx avg `-0.1323` n `6`; index avg `-0.5126` n `25`; metal avg `0.6039` n `20`; unknown avg `2.5879` n `739`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
