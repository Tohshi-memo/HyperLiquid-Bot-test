# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T14:22:24.774585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1632` n `13`; crypto_alt avg `0.2226` n `235`; crypto_major avg `0.0295` n `8`; equity avg `0.0127` n `150`; fx avg `0.0084` n `6`; index avg `0.0006` n `26`; metal avg `0.0042` n `20`; unknown avg `29.0465` n `1134`
- 1h: commodity avg `-0.1841` n `13`; crypto_alt avg `0.1725` n `235`; crypto_major avg `-0.0038` n `8`; equity avg `-0.0138` n `150`; fx avg `-0.017` n `6`; index avg `0.0114` n `26`; metal avg `0.0063` n `20`; unknown avg `27.936` n `1132`
- 4h: commodity avg `-0.2291` n `13`; crypto_alt avg `0.3916` n `235`; crypto_major avg `0.0981` n `8`; equity avg `0.0735` n `150`; fx avg `-0.0015` n `6`; index avg `0.0044` n `26`; metal avg `0.0118` n `20`; unknown avg `5.9745` n `1053`
- 24h: commodity avg `0.1165` n `13`; crypto_alt avg `1.1111` n `235`; crypto_major avg `-0.2419` n `8`; equity avg `0.1372` n `150`; fx avg `0.0116` n `6`; index avg `0.0056` n `26`; metal avg `0.0115` n `20`; unknown avg `1.3036` n `941`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
