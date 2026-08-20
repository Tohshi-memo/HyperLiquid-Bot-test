# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T14:52:16.560976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.5772` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `0.0688` n `230`; crypto_major avg `0.046` n `8`; equity avg `0.022` n `121`; fx avg `0.0017` n `6`; index avg `0.0048` n `25`; metal avg `0.0744` n `20`; unknown avg `-0.0344` n `792`
- 1h: commodity avg `-0.1187` n `12`; crypto_alt avg `0.1452` n `230`; crypto_major avg `0.3104` n `8`; equity avg `0.5554` n `121`; fx avg `-0.0072` n `6`; index avg `0.0815` n `25`; metal avg `0.1608` n `20`; unknown avg `-0.1609` n `792`
- 4h: commodity avg `-0.1598` n `12`; crypto_alt avg `0.2177` n `230`; crypto_major avg `0.6488` n `8`; equity avg `-0.9284` n `121`; fx avg `-0.0145` n `6`; index avg `-0.1103` n `25`; metal avg `0.0916` n `20`; unknown avg `0.2491` n `792`
- 24h: commodity avg `-0.0255` n `12`; crypto_alt avg `6.9617` n `230`; crypto_major avg `11.5875` n `8`; equity avg `0.1997` n `121`; fx avg `0.1867` n `6`; index avg `0.0155` n `25`; metal avg `0.3007` n `20`; unknown avg `2.4608` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
