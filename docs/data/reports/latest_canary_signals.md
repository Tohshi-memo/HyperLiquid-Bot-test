# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T12:22:29.917670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6507` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6024` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0331` n `12`; crypto_alt avg `-0.0041` n `231`; crypto_major avg `0.0836` n `8`; equity avg `0.0293` n `122`; fx avg `-0.0136` n `6`; index avg `-0.0004` n `25`; metal avg `0.015` n `20`; unknown avg `-0.0063` n `793`
- 1h: commodity avg `0.0885` n `12`; crypto_alt avg `0.4099` n `231`; crypto_major avg `0.6636` n `8`; equity avg `0.1762` n `122`; fx avg `-0.0261` n `6`; index avg `0.0369` n `25`; metal avg `0.0812` n `20`; unknown avg `0.2401` n `793`
- 4h: commodity avg `0.1827` n `12`; crypto_alt avg `1.2284` n `231`; crypto_major avg `1.6962` n `8`; equity avg `0.0455` n `122`; fx avg `-0.0343` n `6`; index avg `0.0132` n `25`; metal avg `0.0938` n `20`; unknown avg `1.0958` n `793`
- 24h: commodity avg `-0.0032` n `12`; crypto_alt avg `1.1147` n `231`; crypto_major avg `0.7239` n `8`; equity avg `-1.5097` n `122`; fx avg `-0.1421` n `6`; index avg `-0.147` n `25`; metal avg `0.1988` n `20`; unknown avg `4.3194` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
