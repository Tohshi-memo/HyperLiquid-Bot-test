# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T14:37:30.380307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.5189` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.3746` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.8705` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `0.6744` n `234`; crypto_major avg `0.5225` n `8`; equity avg `0.233` n `141`; fx avg `-0.0062` n `6`; index avg `0.0195` n `26`; metal avg `0.0023` n `20`; unknown avg `3.5345` n `943`
- 1h: commodity avg `0.104` n `12`; crypto_alt avg `1.7983` n `234`; crypto_major avg `0.777` n `8`; equity avg `0.182` n `141`; fx avg `0.009` n `6`; index avg `0.0032` n `26`; metal avg `-0.0024` n `20`; unknown avg `5.1265` n `941`
- 4h: commodity avg `0.1555` n `12`; crypto_alt avg `4.1278` n `234`; crypto_major avg `2.5301` n `8`; equity avg `0.6596` n `141`; fx avg `-0.0353` n `6`; index avg `0.0865` n `26`; metal avg `0.0112` n `20`; unknown avg `11.5497` n `935`
- 24h: commodity avg `0.6591` n `12`; crypto_alt avg `1.6954` n `234`; crypto_major avg `0.3675` n `8`; equity avg `-0.7852` n `141`; fx avg `-0.0047` n `6`; index avg `-0.1742` n `26`; metal avg `-0.2066` n `20`; unknown avg `0.0779` n `811`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
