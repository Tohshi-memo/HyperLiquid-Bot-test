# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T04:07:24.320896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `13`; crypto_alt avg `0.2266` n `235`; crypto_major avg `0.1749` n `8`; equity avg `0.0383` n `150`; fx avg `0.0072` n `6`; index avg `0.0043` n `26`; metal avg `0.0042` n `20`; unknown avg `-0.0468` n `1108`
- 1h: commodity avg `0.0288` n `13`; crypto_alt avg `-0.0523` n `235`; crypto_major avg `0.0401` n `8`; equity avg `0.0404` n `150`; fx avg `0.0068` n `6`; index avg `0.0064` n `26`; metal avg `0.0052` n `20`; unknown avg `-0.1676` n `1108`
- 4h: commodity avg `-0.0017` n `13`; crypto_alt avg `0.7426` n `235`; crypto_major avg `0.4846` n `8`; equity avg `0.1334` n `150`; fx avg `0.0068` n `6`; index avg `0.0292` n `26`; metal avg `0.0155` n `20`; unknown avg `0.028` n `1108`
- 24h: commodity avg `0.0378` n `13`; crypto_alt avg `2.0478` n `235`; crypto_major avg `0.1766` n `8`; equity avg `0.3872` n `150`; fx avg `-0.0162` n `6`; index avg `0.0587` n `26`; metal avg `0.151` n `20`; unknown avg `13.0194` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
