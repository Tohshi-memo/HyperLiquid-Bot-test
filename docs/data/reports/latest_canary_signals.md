# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T08:22:28.062654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0158` n `12`; crypto_alt avg `0.0058` n `230`; crypto_major avg `0.0349` n `8`; equity avg `-0.1263` n `120`; fx avg `0.0122` n `6`; index avg `-0.0173` n `25`; metal avg `-0.0156` n `20`; unknown avg `0.0197` n `789`
- 1h: commodity avg `-0.0497` n `12`; crypto_alt avg `0.1031` n `230`; crypto_major avg `-0.025` n `8`; equity avg `0.5341` n `120`; fx avg `-0.0502` n `6`; index avg `0.0872` n `25`; metal avg `0.0474` n `20`; unknown avg `0.0264` n `789`
- 4h: commodity avg `-0.0244` n `12`; crypto_alt avg `0.1929` n `230`; crypto_major avg `-0.0044` n `8`; equity avg `1.0834` n `120`; fx avg `-0.0472` n `6`; index avg `0.2056` n `25`; metal avg `0.0348` n `20`; unknown avg `-0.017` n `757`
- 24h: commodity avg `0.2473` n `12`; crypto_alt avg `0.4047` n `230`; crypto_major avg `0.2892` n `8`; equity avg `-1.2578` n `120`; fx avg `-0.2096` n `6`; index avg `-0.1576` n `25`; metal avg `-0.4342` n `20`; unknown avg `-0.2203` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
