# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T04:21:05.218438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0128` n `12`; crypto_alt avg `0.0696` n `230`; crypto_major avg `0.1155` n `8`; equity avg `-0.058` n `121`; fx avg `-0.0032` n `6`; index avg `-0.015` n `25`; metal avg `0.0423` n `20`; unknown avg `0.0331` n `793`
- 1h: commodity avg `-0.0101` n `12`; crypto_alt avg `0.2022` n `230`; crypto_major avg `0.3902` n `8`; equity avg `-0.1591` n `121`; fx avg `0.002` n `6`; index avg `-0.0251` n `25`; metal avg `0.0572` n `20`; unknown avg `-0.0629` n `793`
- 4h: commodity avg `0.0537` n `12`; crypto_alt avg `0.5852` n `230`; crypto_major avg `0.7209` n `8`; equity avg `0.4118` n `121`; fx avg `-0.0379` n `6`; index avg `0.0864` n `25`; metal avg `0.273` n `20`; unknown avg `0.0935` n `793`
- 24h: commodity avg `0.284` n `12`; crypto_alt avg `5.7433` n `230`; crypto_major avg `7.186` n `8`; equity avg `-0.7958` n `121`; fx avg `-0.0269` n `6`; index avg `-0.1454` n `25`; metal avg `0.5281` n `20`; unknown avg `2.5652` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
