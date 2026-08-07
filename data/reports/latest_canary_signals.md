# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T13:52:28.278798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0584` n `12`; crypto_alt avg `0.0627` n `230`; crypto_major avg `0.0971` n `8`; equity avg `0.2156` n `112`; fx avg `0.0067` n `6`; index avg `0.0161` n `25`; metal avg `-0.0264` n `20`; unknown avg `-0.0335` n `782`
- 1h: commodity avg `0.2182` n `12`; crypto_alt avg `0.0642` n `230`; crypto_major avg `0.0176` n `8`; equity avg `-0.6341` n `112`; fx avg `0.0313` n `6`; index avg `-0.0848` n `25`; metal avg `-0.1456` n `20`; unknown avg `-0.0443` n `782`
- 4h: commodity avg `0.1006` n `12`; crypto_alt avg `0.0929` n `230`; crypto_major avg `0.4377` n `8`; equity avg `0.5066` n `112`; fx avg `-0.0305` n `6`; index avg `0.1175` n `25`; metal avg `-0.1501` n `20`; unknown avg `-0.1341` n `782`
- 24h: commodity avg `0.4095` n `12`; crypto_alt avg `0.2856` n `230`; crypto_major avg `0.8695` n `8`; equity avg `2.2427` n `109`; fx avg `-0.1224` n `6`; index avg `0.1408` n `25`; metal avg `0.4876` n `20`; unknown avg `0.1705` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
