# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T01:07:28.922553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0267` n `12`; crypto_alt avg `-0.2823` n `230`; crypto_major avg `-0.4641` n `8`; equity avg `0.215` n `121`; fx avg `0.0106` n `6`; index avg `0.0433` n `25`; metal avg `-0.1523` n `20`; unknown avg `-0.0175` n `792`
- 1h: commodity avg `0.0621` n `12`; crypto_alt avg `-0.0217` n `230`; crypto_major avg `-0.1817` n `8`; equity avg `0.7165` n `121`; fx avg `0.0795` n `6`; index avg `0.1902` n `25`; metal avg `-0.1869` n `20`; unknown avg `0.0268` n `792`
- 4h: commodity avg `0.0212` n `12`; crypto_alt avg `-0.5485` n `230`; crypto_major avg `-0.6347` n `8`; equity avg `0.6876` n `121`; fx avg `0.109` n `6`; index avg `0.1418` n `25`; metal avg `-0.243` n `20`; unknown avg `-0.0855` n `792`
- 24h: commodity avg `-0.0652` n `12`; crypto_alt avg `5.2979` n `230`; crypto_major avg `9.407` n `8`; equity avg `1.3255` n `120`; fx avg `-0.0532` n `6`; index avg `0.2101` n `25`; metal avg `1.0268` n `20`; unknown avg `1.4505` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
