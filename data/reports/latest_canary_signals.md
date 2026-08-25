# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T03:11:52.370453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.0372` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.6332` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.3136` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.058` n `12`; crypto_alt avg `0.3006` n `231`; crypto_major avg `0.4734` n `8`; equity avg `0.1621` n `122`; fx avg `0.0033` n `6`; index avg `0.0363` n `25`; metal avg `0.022` n `20`; unknown avg `0.706` n `794`
- 1h: commodity avg `-0.0698` n `12`; crypto_alt avg `0.9671` n `231`; crypto_major avg `1.1462` n `8`; equity avg `0.144` n `122`; fx avg `0.011` n `6`; index avg `0.0454` n `25`; metal avg `-0.0988` n `20`; unknown avg `1.3716` n `794`
- 4h: commodity avg `0.045` n `12`; crypto_alt avg `1.9184` n `231`; crypto_major avg `2.6782` n `8`; equity avg `0.3646` n `122`; fx avg `0.0317` n `6`; index avg `0.0261` n `25`; metal avg `-0.359` n `20`; unknown avg `0.8207` n `794`
- 24h: commodity avg `0.0221` n `12`; crypto_alt avg `2.114` n `231`; crypto_major avg `2.9823` n `8`; equity avg `-0.9969` n `122`; fx avg `0.0213` n `6`; index avg `-0.1886` n `25`; metal avg `-0.1542` n `20`; unknown avg `0.6064` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
