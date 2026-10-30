# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T22:07:39.418008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `13`; crypto_alt avg `0.1542` n `238`; crypto_major avg `0.0793` n `8`; equity avg `0.0789` n `156`; fx avg `-0.0018` n `6`; index avg `0.0102` n `27`; metal avg `0.0142` n `20`; unknown avg `199.1845` n `1255`
- 1h: commodity avg `0.0422` n `13`; crypto_alt avg `0.3994` n `238`; crypto_major avg `-0.0133` n `8`; equity avg `-0.0065` n `156`; fx avg `-0.0701` n `6`; index avg `0.0041` n `27`; metal avg `0.0346` n `20`; unknown avg `199.0716` n `1255`
- 4h: commodity avg `-0.2672` n `13`; crypto_alt avg `0.6574` n `238`; crypto_major avg `-0.1542` n `8`; equity avg `1.0112` n `156`; fx avg `-0.0315` n `6`; index avg `0.095` n `27`; metal avg `0.0695` n `20`; unknown avg `0.2221` n `1149`
- 24h: commodity avg `0.0926` n `13`; crypto_alt avg `1.5841` n `238`; crypto_major avg `-0.9686` n `8`; equity avg `-3.0248` n `156`; fx avg `-0.1403` n `6`; index avg `-0.2819` n `27`; metal avg `-0.9779` n `20`; unknown avg `1.0577` n `1014`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
