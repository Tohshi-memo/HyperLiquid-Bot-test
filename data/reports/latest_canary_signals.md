# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T22:52:30.840837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `4.18` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `4.1534` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `4.0102` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0082` n `12`; crypto_alt avg `0.1559` n `230`; crypto_major avg `0.2327` n `8`; equity avg `-0.0031` n `121`; fx avg `-0.0073` n `6`; index avg `0.0046` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.1083` n `793`
- 1h: commodity avg `0.0408` n `12`; crypto_alt avg `0.5746` n `230`; crypto_major avg `0.905` n `8`; equity avg `0.0109` n `121`; fx avg `-0.0141` n `6`; index avg `0.015` n `25`; metal avg `-0.0197` n `20`; unknown avg `0.9638` n `793`
- 4h: commodity avg `-0.0375` n `12`; crypto_alt avg `2.7941` n `230`; crypto_major avg `4.1159` n `8`; equity avg `0.1057` n `121`; fx avg `-0.0114` n `6`; index avg `0.0106` n `25`; metal avg `-0.0641` n `20`; unknown avg `0.6551` n `793`
- 24h: commodity avg `0.1761` n `12`; crypto_alt avg `8.9493` n `230`; crypto_major avg `8.379` n `8`; equity avg `0.9242` n `121`; fx avg `-0.0705` n `6`; index avg `0.1019` n `25`; metal avg `0.4521` n `20`; unknown avg `2.0071` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1706`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
