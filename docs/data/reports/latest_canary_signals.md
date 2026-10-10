# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T03:07:25.321057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0132` n `13`; crypto_alt avg `0.0598` n `235`; crypto_major avg `-0.0352` n `8`; equity avg `0.0028` n `150`; fx avg `0.0` n `6`; index avg `-0.0026` n `26`; metal avg `0.0068` n `20`; unknown avg `0.0171` n `1114`
- 1h: commodity avg `-0.0056` n `13`; crypto_alt avg `0.0927` n `235`; crypto_major avg `-0.0675` n `8`; equity avg `0.0165` n `150`; fx avg `0.0006` n `6`; index avg `-0.0043` n `26`; metal avg `0.007` n `20`; unknown avg `0.3134` n `1114`
- 4h: commodity avg `-0.0152` n `13`; crypto_alt avg `1.129` n `235`; crypto_major avg `0.41` n `8`; equity avg `0.0798` n `150`; fx avg `0.0033` n `6`; index avg `0.0277` n `26`; metal avg `0.0191` n `20`; unknown avg `0.091` n `1108`
- 24h: commodity avg `-0.0412` n `13`; crypto_alt avg `2.5863` n `235`; crypto_major avg `0.4109` n `8`; equity avg `0.6511` n `150`; fx avg `-0.0174` n `6`; index avg `0.0847` n `26`; metal avg `0.1904` n `20`; unknown avg `13.5096` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
