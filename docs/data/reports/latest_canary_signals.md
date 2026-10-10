# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T15:07:26.845134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `13`; crypto_alt avg `-0.0282` n `235`; crypto_major avg `0.0441` n `8`; equity avg `-0.0051` n `150`; fx avg `0.0` n `6`; index avg `-0.0033` n `26`; metal avg `-0.002` n `20`; unknown avg `1.5743` n `1115`
- 1h: commodity avg `0.0146` n `13`; crypto_alt avg `0.6507` n `235`; crypto_major avg `0.637` n `8`; equity avg `0.1145` n `150`; fx avg `0.003` n `6`; index avg `0.0228` n `26`; metal avg `0.0022` n `20`; unknown avg `0.284` n `1115`
- 4h: commodity avg `0.0882` n `13`; crypto_alt avg `0.9667` n `235`; crypto_major avg `0.7458` n `8`; equity avg `0.139` n `150`; fx avg `-0.0113` n `6`; index avg `0.0081` n `26`; metal avg `0.001` n `20`; unknown avg `1.5182` n `1109`
- 24h: commodity avg `-0.5638` n `13`; crypto_alt avg `2.9408` n `235`; crypto_major avg `1.1618` n `8`; equity avg `0.4866` n `150`; fx avg `0.0053` n `6`; index avg `0.0828` n `26`; metal avg `0.0426` n `20`; unknown avg `1.695` n `936`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
