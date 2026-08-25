# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T02:52:30.714746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.504` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.0506` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.9196` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0351` n `12`; crypto_alt avg `-0.3473` n `231`; crypto_major avg `-0.4478` n `8`; equity avg `-0.1627` n `122`; fx avg `0.0027` n `6`; index avg `-0.0362` n `25`; metal avg `-0.1198` n `20`; unknown avg `0.2236` n `794`
- 1h: commodity avg `0.0327` n `12`; crypto_alt avg `0.7377` n `231`; crypto_major avg `0.8545` n `8`; equity avg `0.0049` n `122`; fx avg `0.0008` n `6`; index avg `-0.013` n `25`; metal avg `-0.3319` n `20`; unknown avg `0.2651` n `794`
- 4h: commodity avg `0.1096` n `12`; crypto_alt avg `1.4127` n `231`; crypto_major avg `2.1602` n `8`; equity avg `0.2406` n `122`; fx avg `0.0311` n `6`; index avg `-0.0112` n `25`; metal avg `-0.3438` n `20`; unknown avg `0.1898` n `794`
- 24h: commodity avg `0.1154` n `12`; crypto_alt avg `1.5933` n `231`; crypto_major avg `2.3181` n `8`; equity avg `-1.375` n `122`; fx avg `0.0324` n `6`; index avg `-0.2537` n `25`; metal avg `-0.1434` n `20`; unknown avg `0.5594` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
