# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T11:07:30.382886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `13`; crypto_alt avg `-0.0258` n `235`; crypto_major avg `-0.0455` n `8`; equity avg `0.0054` n `150`; fx avg `0.0011` n `6`; index avg `0.0031` n `26`; metal avg `0.0056` n `20`; unknown avg `0.1436` n `1115`
- 1h: commodity avg `-0.0044` n `13`; crypto_alt avg `-0.0374` n `235`; crypto_major avg `-0.0831` n `8`; equity avg `-0.0004` n `150`; fx avg `0.0108` n `6`; index avg `0.0006` n `26`; metal avg `0.0033` n `20`; unknown avg `0.1445` n `1115`
- 4h: commodity avg `-0.2514` n `13`; crypto_alt avg `-0.2939` n `235`; crypto_major avg `-0.1046` n `8`; equity avg `-0.0147` n `150`; fx avg `0.0064` n `6`; index avg `-0.0036` n `26`; metal avg `0.0041` n `20`; unknown avg `0.1975` n `1099`
- 24h: commodity avg `-0.142` n `13`; crypto_alt avg `1.8757` n `235`; crypto_major avg `0.272` n `8`; equity avg `-0.123` n `150`; fx avg `0.0228` n `6`; index avg `0.0016` n `26`; metal avg `0.1018` n `20`; unknown avg `631.7906` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
