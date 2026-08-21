# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T09:37:38.775239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3577` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1927` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8928` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.044` n `12`; crypto_alt avg `0.9759` n `230`; crypto_major avg `0.8632` n `8`; equity avg `0.1318` n `121`; fx avg `-0.0104` n `6`; index avg `0.0087` n `25`; metal avg `-0.0588` n `20`; unknown avg `0.072` n `793`
- 1h: commodity avg `0.0544` n `12`; crypto_alt avg `-0.0969` n `230`; crypto_major avg `0.1614` n `8`; equity avg `0.1448` n `121`; fx avg `0.0315` n `6`; index avg `-0.0091` n `25`; metal avg `-0.0953` n `20`; unknown avg `0.1221` n `793`
- 4h: commodity avg `0.1049` n `12`; crypto_alt avg `2.4898` n `230`; crypto_major avg `2.4626` n `8`; equity avg `0.5698` n `121`; fx avg `0.0085` n `6`; index avg `0.016` n `25`; metal avg `0.2699` n `20`; unknown avg `0.2982` n `777`
- 24h: commodity avg `0.0784` n `12`; crypto_alt avg `6.6214` n `230`; crypto_major avg `6.8935` n `8`; equity avg `0.5592` n `121`; fx avg `-0.0896` n `6`; index avg `0.0258` n `25`; metal avg `0.89` n `20`; unknown avg `2.4665` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
