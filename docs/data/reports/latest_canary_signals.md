# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T02:07:28.040674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `13`; crypto_alt avg `0.111` n `235`; crypto_major avg `0.0522` n `8`; equity avg `0.1162` n `151`; fx avg `-0.0174` n `6`; index avg `0.0267` n `26`; metal avg `0.0638` n `20`; unknown avg `0.0122` n `1133`
- 1h: commodity avg `-0.0305` n `13`; crypto_alt avg `0.2767` n `235`; crypto_major avg `0.1336` n `8`; equity avg `0.143` n `151`; fx avg `-0.0387` n `6`; index avg `0.0528` n `26`; metal avg `0.029` n `20`; unknown avg `0.0117` n `1133`
- 4h: commodity avg `0.1291` n `13`; crypto_alt avg `0.3497` n `235`; crypto_major avg `0.2481` n `8`; equity avg `0.1901` n `151`; fx avg `-0.0016` n `6`; index avg `0.0506` n `26`; metal avg `-0.005` n `20`; unknown avg `0.4413` n `1127`
- 24h: commodity avg `1.0387` n `13`; crypto_alt avg `1.6205` n `235`; crypto_major avg `1.2215` n `8`; equity avg `1.0501` n `151`; fx avg `0.105` n `6`; index avg `0.2` n `26`; metal avg `-0.1965` n `20`; unknown avg `1.0126` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1552`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1409`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0924`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `666`, weak_sample_signal
