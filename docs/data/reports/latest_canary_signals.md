# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T16:07:28.765058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.5296` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.4446` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7299` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `-0.0361` n `230`; crypto_major avg `0.0411` n `8`; equity avg `-0.1588` n `121`; fx avg `-0.0004` n `6`; index avg `0.0011` n `25`; metal avg `0.014` n `20`; unknown avg `0.0191` n `792`
- 1h: commodity avg `0.0747` n `12`; crypto_alt avg `0.2676` n `230`; crypto_major avg `0.8386` n `8`; equity avg `-0.4728` n `121`; fx avg `0.0216` n `6`; index avg `-0.0712` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.0166` n `792`
- 4h: commodity avg `-0.1414` n `12`; crypto_alt avg `1.3058` n `230`; crypto_major avg `2.3032` n `8`; equity avg `-0.2264` n `121`; fx avg `-0.0107` n `6`; index avg `0.0638` n `25`; metal avg `0.5733` n `20`; unknown avg `0.0926` n `792`
- 24h: commodity avg `-0.0163` n `12`; crypto_alt avg `6.0474` n `230`; crypto_major avg `9.2257` n `8`; equity avg `-1.0792` n `121`; fx avg `0.162` n `6`; index avg `-0.1058` n `25`; metal avg `0.2968` n `20`; unknown avg `2.2051` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
