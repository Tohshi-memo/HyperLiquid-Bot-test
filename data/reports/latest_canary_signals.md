# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T14:22:31.141204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6021` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1564` n `12`; crypto_alt avg `-0.1438` n `230`; crypto_major avg `0.1676` n `8`; equity avg `0.1129` n `121`; fx avg `-0.0142` n `6`; index avg `0.0109` n `25`; metal avg `0.0403` n `20`; unknown avg `-0.1309` n `792`
- 1h: commodity avg `-0.1223` n `12`; crypto_alt avg `0.085` n `230`; crypto_major avg `0.2411` n `8`; equity avg `0.0674` n `121`; fx avg `0.0135` n `6`; index avg `0.0774` n `25`; metal avg `0.0571` n `20`; unknown avg `-0.0412` n `792`
- 4h: commodity avg `-0.0985` n `12`; crypto_alt avg `0.3062` n `230`; crypto_major avg `0.621` n `8`; equity avg `-0.9811` n `121`; fx avg `-0.0046` n `6`; index avg `-0.113` n `25`; metal avg `0.0059` n `20`; unknown avg `0.222` n `792`
- 24h: commodity avg `0.045` n `12`; crypto_alt avg `7.4622` n `230`; crypto_major avg `12.4461` n `8`; equity avg `0.9126` n `121`; fx avg `0.1802` n `6`; index avg `0.1054` n `25`; metal avg `0.2598` n `20`; unknown avg `2.5023` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1895`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
