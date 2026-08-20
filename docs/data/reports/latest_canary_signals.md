# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T12:22:26.680515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.1269` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0507` n `12`; crypto_alt avg `0.0896` n `230`; crypto_major avg `0.0276` n `8`; equity avg `-0.2226` n `121`; fx avg `0.0046` n `6`; index avg `-0.0185` n `25`; metal avg `0.0975` n `20`; unknown avg `-0.0145` n `792`
- 1h: commodity avg `0.0833` n `12`; crypto_alt avg `0.0501` n `230`; crypto_major avg `-0.1226` n `8`; equity avg `-0.9389` n `121`; fx avg `0.0028` n `6`; index avg `-0.1646` n `25`; metal avg `-0.1732` n `20`; unknown avg `0.0963` n `792`
- 4h: commodity avg `0.2948` n `12`; crypto_alt avg `0.8205` n `230`; crypto_major avg `0.8535` n `8`; equity avg `-1.2734` n `121`; fx avg `0.0569` n `6`; index avg `-0.226` n `25`; metal avg `-0.2339` n `20`; unknown avg `0.2155` n `792`
- 24h: commodity avg `0.2968` n `12`; crypto_alt avg `7.4323` n `230`; crypto_major avg `12.1305` n `8`; equity avg `-0.7635` n `120`; fx avg `0.2486` n `6`; index avg `-0.1404` n `25`; metal avg `0.621` n `20`; unknown avg `2.4984` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
