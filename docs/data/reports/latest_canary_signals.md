# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T04:37:26.644478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7753` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7581` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.7275` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.1457` n `230`; crypto_major avg `-0.2221` n `8`; equity avg `-0.0024` n `121`; fx avg `0.0041` n `6`; index avg `0.0011` n `25`; metal avg `-0.0037` n `20`; unknown avg `-0.0481` n `794`
- 1h: commodity avg `-0.0089` n `12`; crypto_alt avg `-0.303` n `230`; crypto_major avg `-0.3464` n `8`; equity avg `-0.012` n `121`; fx avg `0.0024` n `6`; index avg `0.0016` n `25`; metal avg `-0.0111` n `20`; unknown avg `-0.1714` n `794`
- 4h: commodity avg `-0.0424` n `12`; crypto_alt avg `-2.9028` n `230`; crypto_major avg `-1.7581` n `8`; equity avg `-0.0306` n `121`; fx avg `0.0113` n `6`; index avg `0.0172` n `25`; metal avg `-0.0` n `20`; unknown avg `2.5034` n `794`
- 24h: commodity avg `0.0379` n `12`; crypto_alt avg `-8.71` n `230`; crypto_major avg `-5.4062` n `8`; equity avg `-0.2967` n `121`; fx avg `0.0907` n `6`; index avg `-0.0182` n `25`; metal avg `-0.0099` n `20`; unknown avg `2.0181` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
