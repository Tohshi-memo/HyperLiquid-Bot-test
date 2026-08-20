# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T10:07:24.977403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.9932` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.6946` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.3349` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `0.2582` n `230`; crypto_major avg `0.305` n `8`; equity avg `0.082` n `121`; fx avg `-0.0071` n `6`; index avg `0.0119` n `25`; metal avg `0.0313` n `20`; unknown avg `-0.0456` n `792`
- 1h: commodity avg `0.0417` n `12`; crypto_alt avg `-0.0151` n `230`; crypto_major avg `-0.157` n `8`; equity avg `0.0498` n `121`; fx avg `-0.002` n `6`; index avg `0.0185` n `25`; metal avg `0.0195` n `20`; unknown avg `0.0619` n `792`
- 4h: commodity avg `0.3159` n `12`; crypto_alt avg `2.118` n `230`; crypto_major avg `2.6508` n `8`; equity avg `-0.3424` n `121`; fx avg `0.0491` n `6`; index avg `-0.0789` n `25`; metal avg `-0.0438` n `20`; unknown avg `0.6249` n `792`
- 24h: commodity avg `0.1982` n `12`; crypto_alt avg `7.5583` n `230`; crypto_major avg `12.6007` n `8`; equity avg `0.6998` n `120`; fx avg `0.2024` n `6`; index avg `0.1401` n `25`; metal avg `0.9373` n `20`; unknown avg `2.3055` n `775`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
