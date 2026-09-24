# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T15:37:39.074561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.2022` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0143` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.2013` n `12`; crypto_alt avg `0.7714` n `234`; crypto_major avg `0.6025` n `8`; equity avg `0.0548` n `141`; fx avg `-0.0011` n `6`; index avg `0.0013` n `26`; metal avg `-0.032` n `20`; unknown avg `0.3435` n `943`
- 1h: commodity avg `0.7263` n `12`; crypto_alt avg `-0.167` n `234`; crypto_major avg `0.0071` n `8`; equity avg `-0.4571` n `141`; fx avg `0.0286` n `6`; index avg `-0.0852` n `26`; metal avg `-0.1047` n `20`; unknown avg `5.0845` n `895`
- 4h: commodity avg `0.8428` n `12`; crypto_alt avg `3.2756` n `234`; crypto_major avg `2.086` n `8`; equity avg `0.0717` n `141`; fx avg `-0.004` n `6`; index avg `-0.019` n `26`; metal avg `-0.1162` n `20`; unknown avg `4.9957` n `889`
- 24h: commodity avg `1.1154` n `12`; crypto_alt avg `2.554` n `234`; crypto_major avg `0.8382` n `8`; equity avg `-1.528` n `141`; fx avg `0.0258` n `6`; index avg `-0.27` n `26`; metal avg `-0.2282` n `20`; unknown avg `265.5222` n `823`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
