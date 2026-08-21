# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T22:07:33.809829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.3229` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.2864` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.1291` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `2.5923` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `2.5873` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `2.5404` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0198` n `12`; crypto_alt avg `0.4567` n `230`; crypto_major avg `0.8597` n `8`; equity avg `0.0147` n `121`; fx avg `-0.0084` n `6`; index avg `0.0078` n `25`; metal avg `-0.0102` n `20`; unknown avg `1.218` n `793`
- 1h: commodity avg `0.0026` n `12`; crypto_alt avg `1.4253` n `230`; crypto_major avg `2.5899` n `8`; equity avg `0.0495` n `121`; fx avg `0.0038` n `6`; index avg `0.0178` n `25`; metal avg `-0.0024` n `20`; unknown avg `1.0173` n `793`
- 4h: commodity avg `-0.0947` n `12`; crypto_alt avg `1.6513` n `230`; crypto_major avg `3.2282` n `8`; equity avg `0.0991` n `121`; fx avg `-0.0086` n `6`; index avg `0.0047` n `25`; metal avg `-0.0582` n `20`; unknown avg `0.9116` n `793`
- 24h: commodity avg `0.1533` n `12`; crypto_alt avg `8.9233` n `230`; crypto_major avg `8.4668` n `8`; equity avg `1.0499` n `121`; fx avg `-0.0691` n `6`; index avg `0.127` n `25`; metal avg `0.5279` n `20`; unknown avg `2.4492` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
