# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T08:37:30.260875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6179` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2958` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9565` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `1.5562` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0502` n `12`; crypto_alt avg `0.4047` n `230`; crypto_major avg `0.6228` n `8`; equity avg `0.293` n `121`; fx avg `-0.0162` n `6`; index avg `0.0413` n `25`; metal avg `0.108` n `20`; unknown avg `0.1103` n `793`
- 1h: commodity avg `-0.0562` n `12`; crypto_alt avg `1.3314` n `230`; crypto_major avg `1.5371` n `8`; equity avg `-0.0191` n `121`; fx avg `-0.0422` n `6`; index avg `-0.0264` n `25`; metal avg `0.2602` n `20`; unknown avg `0.1428` n `793`
- 4h: commodity avg `0.0215` n `12`; crypto_alt avg `3.0322` n `230`; crypto_major avg `2.6394` n `8`; equity avg `0.6829` n `121`; fx avg `-0.0284` n `6`; index avg `0.0748` n `25`; metal avg `0.3436` n `20`; unknown avg `0.2322` n `777`
- 24h: commodity avg `0.0638` n `12`; crypto_alt avg `7.2298` n `230`; crypto_major avg `7.3124` n `8`; equity avg `0.6606` n `121`; fx avg `-0.0926` n `6`; index avg `0.0589` n `25`; metal avg `0.9586` n `20`; unknown avg `2.5181` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2026`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1975`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
