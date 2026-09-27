# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T01:47:08.689437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `74.54` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `0.218` n `234`; crypto_major avg `0.1243` n `8`; equity avg `0.039` n `141`; fx avg `0.0009` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.0304` n `961`
- 1h: commodity avg `0.0132` n `12`; crypto_alt avg `0.3715` n `234`; crypto_major avg `0.1462` n `8`; equity avg `0.0059` n `141`; fx avg `-0.0053` n `6`; index avg `0.0002` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.1162` n `959`
- 4h: commodity avg `-0.0606` n `12`; crypto_alt avg `0.4025` n `234`; crypto_major avg `0.2167` n `8`; equity avg `0.0968` n `141`; fx avg `-0.0053` n `6`; index avg `0.0036` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.1414` n `927`
- 24h: commodity avg `-0.1023` n `12`; crypto_alt avg `0.6943` n `234`; crypto_major avg `-0.7917` n `8`; equity avg `0.1959` n `141`; fx avg `0.0127` n `6`; index avg `-0.0002` n `26`; metal avg `-0.007` n `20`; unknown avg `4.0999` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
