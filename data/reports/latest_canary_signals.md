# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T18:52:30.828403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1918` n `13`; crypto_alt avg `-0.1839` n `235`; crypto_major avg `-0.0785` n `8`; equity avg `0.0245` n `150`; fx avg `-0.0024` n `6`; index avg `0.0196` n `26`; metal avg `0.02` n `20`; unknown avg `2.4782` n `1092`
- 1h: commodity avg `-0.23` n `13`; crypto_alt avg `-0.2243` n `235`; crypto_major avg `-0.1481` n `8`; equity avg `0.0246` n `150`; fx avg `0.0119` n `6`; index avg `0.0362` n `26`; metal avg `0.0413` n `20`; unknown avg `3.2537` n `1090`
- 4h: commodity avg `-0.3729` n `13`; crypto_alt avg `0.1565` n `235`; crypto_major avg `-0.3606` n `8`; equity avg `0.2534` n `150`; fx avg `-0.0067` n `6`; index avg `0.0482` n `26`; metal avg `0.067` n `20`; unknown avg `2.0094` n `1020`
- 24h: commodity avg `-0.2172` n `13`; crypto_alt avg `2.7557` n `235`; crypto_major avg `1.3316` n `8`; equity avg `1.3156` n `150`; fx avg `0.0315` n `6`; index avg `0.22` n `26`; metal avg `0.6769` n `20`; unknown avg `2.0472` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1517`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.139`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1327`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1304`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1132`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0975`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `669`, weak_sample_signal
