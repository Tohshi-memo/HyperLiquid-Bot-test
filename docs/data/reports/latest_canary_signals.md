# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T21:52:27.616018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5851` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4766` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.4579` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.2168` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `2.1803` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `2.1692` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `0.3015` n `230`; crypto_major avg `0.5461` n `8`; equity avg `0.0196` n `121`; fx avg `0.0` n `6`; index avg `0.0048` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.2408` n `793`
- 1h: commodity avg `-0.0109` n `12`; crypto_alt avg `1.3759` n `230`; crypto_major avg `2.2059` n `8`; equity avg `0.0256` n `121`; fx avg `0.0162` n `6`; index avg `0.0098` n `25`; metal avg `0.0367` n `20`; unknown avg `-0.2084` n `793`
- 4h: commodity avg `-0.1186` n `12`; crypto_alt avg `1.4724` n `230`; crypto_major avg `2.4665` n `8`; equity avg `0.0086` n `121`; fx avg `0.0109` n `6`; index avg `-0.0085` n `25`; metal avg `-0.0101` n `20`; unknown avg `-0.3091` n `793`
- 24h: commodity avg `0.1409` n `12`; crypto_alt avg `8.4488` n `230`; crypto_major avg `7.0912` n `8`; equity avg `0.9349` n `121`; fx avg `-0.0776` n `6`; index avg `0.1083` n `25`; metal avg `0.5423` n `20`; unknown avg `1.166` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.182`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
