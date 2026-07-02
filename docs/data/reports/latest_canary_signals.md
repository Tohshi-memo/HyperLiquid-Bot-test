# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T11:37:27.310873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6899` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2909` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6303` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0999` n `12`; crypto_alt avg `-0.0016` n `229`; crypto_major avg `0.0403` n `8`; equity avg `0.0422` n `88`; fx avg `0.0028` n `6`; index avg `0.0079` n `25`; metal avg `0.0106` n `20`; unknown avg `-0.0973` n `763`
- 1h: commodity avg `-0.2057` n `12`; crypto_alt avg `0.1717` n `229`; crypto_major avg `0.5448` n `8`; equity avg `0.148` n `88`; fx avg `-0.0054` n `6`; index avg `-0.0096` n `25`; metal avg `-0.0041` n `20`; unknown avg `-0.0327` n `763`
- 4h: commodity avg `-0.276` n `12`; crypto_alt avg `1.5102` n `228`; crypto_major avg `2.4139` n `8`; equity avg `0.7836` n `88`; fx avg `-0.0334` n `6`; index avg `0.0671` n `25`; metal avg `0.123` n `20`; unknown avg `0.7712` n `763`
- 24h: commodity avg `-0.6275` n `12`; crypto_alt avg `3.0732` n `228`; crypto_major avg `4.1931` n `8`; equity avg `-1.8295` n `88`; fx avg `-0.1194` n `6`; index avg `-0.5627` n `25`; metal avg `0.6533` n `20`; unknown avg `2.211` n `739`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
