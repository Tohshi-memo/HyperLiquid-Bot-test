# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T06:52:31.654890+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0281` n `13`; crypto_alt avg `0.0039` n `239`; crypto_major avg `-0.1047` n `8`; equity avg `-0.0333` n `162`; fx avg `-0.0102` n `6`; index avg `0.0037` n `27`; metal avg `0.0212` n `20`; unknown avg `0.2916` n `1262`
- 1h: commodity avg `0.121` n `13`; crypto_alt avg `1.0048` n `239`; crypto_major avg `0.4967` n `8`; equity avg `0.0608` n `162`; fx avg `0.017` n `6`; index avg `-0.0089` n `27`; metal avg `0.0114` n `20`; unknown avg `162.8046` n `1228`
- 4h: commodity avg `0.0511` n `13`; crypto_alt avg `0.0742` n `239`; crypto_major avg `-0.8891` n `8`; equity avg `-1.1684` n `162`; fx avg `0.0333` n `6`; index avg `-0.1509` n `27`; metal avg `-0.1984` n `20`; unknown avg `1.1568` n `1216`
- 24h: commodity avg `0.7622` n `13`; crypto_alt avg `-1.2683` n `239`; crypto_major avg `-3.2354` n `8`; equity avg `-1.0416` n `162`; fx avg `-0.0053` n `6`; index avg `0.0306` n `27`; metal avg `-0.537` n `20`; unknown avg `98.3951` n `1133`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
