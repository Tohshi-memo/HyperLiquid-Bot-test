# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T08:55:39.833176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.6569` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.3996` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.9852` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.7611` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.5859` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.539` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0164` n `12`; crypto_alt avg `0.9492` n `230`; crypto_major avg `1.1774` n `8`; equity avg `0.1593` n `121`; fx avg `0.0182` n `6`; index avg `0.0137` n `25`; metal avg `-0.0555` n `20`; unknown avg `0.1458` n `793`
- 1h: commodity avg `-0.0476` n `12`; crypto_alt avg `1.842` n `230`; crypto_major avg `2.7135` n `8`; equity avg `0.1745` n `121`; fx avg `-0.0122` n `6`; index avg `-0.0142` n `25`; metal avg `0.1276` n `20`; unknown avg `0.4086` n `793`
- 4h: commodity avg `0.0346` n `12`; crypto_alt avg `3.86` n `230`; crypto_major avg `3.6915` n `8`; equity avg `0.7063` n `121`; fx avg `-0.0002` n `6`; index avg `0.0436` n `25`; metal avg `0.2919` n `20`; unknown avg `0.4405` n `777`
- 24h: commodity avg `0.0281` n `12`; crypto_alt avg `8.1` n `230`; crypto_major avg `8.3171` n `8`; equity avg `0.7755` n `121`; fx avg `-0.1057` n `6`; index avg `0.0812` n `25`; metal avg `0.932` n `20`; unknown avg `2.6857` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2073`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2007`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
