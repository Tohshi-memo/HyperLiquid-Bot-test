# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T22:52:30.864522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `13`; crypto_alt avg `-0.2045` n `235`; crypto_major avg `-0.0665` n `8`; equity avg `-0.0021` n `150`; fx avg `-0.0034` n `6`; index avg `0.0001` n `26`; metal avg `-0.0022` n `20`; unknown avg `5.6689` n `1117`
- 1h: commodity avg `0.0316` n `13`; crypto_alt avg `-0.2438` n `235`; crypto_major avg `-0.0944` n `8`; equity avg `0.0012` n `150`; fx avg `-0.0006` n `6`; index avg `0.0041` n `26`; metal avg `0.002` n `20`; unknown avg `4.8811` n `1107`
- 4h: commodity avg `0.1967` n `13`; crypto_alt avg `0.1298` n `235`; crypto_major avg `-0.0483` n `8`; equity avg `0.0607` n `150`; fx avg `-0.0029` n `6`; index avg `0.0111` n `26`; metal avg `0.0165` n `20`; unknown avg `4.4502` n `1023`
- 24h: commodity avg `0.0724` n `13`; crypto_alt avg `2.2328` n `235`; crypto_major avg `0.7018` n `8`; equity avg `0.1911` n `150`; fx avg `-0.0067` n `6`; index avg `0.0218` n `26`; metal avg `0.0098` n `20`; unknown avg `0.1733` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
