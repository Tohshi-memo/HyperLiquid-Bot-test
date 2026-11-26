# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T21:22:29.180956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `13`; crypto_alt avg `0.079` n `239`; crypto_major avg `0.0115` n `8`; equity avg `0.0566` n `168`; fx avg `-0.0008` n `6`; index avg `0.0049` n `27`; metal avg `0.0003` n `20`; unknown avg `1.0583` n `1259`
- 1h: commodity avg `-0.0075` n `13`; crypto_alt avg `0.153` n `239`; crypto_major avg `0.2228` n `8`; equity avg `0.1357` n `168`; fx avg `0.0002` n `6`; index avg `0.0109` n `27`; metal avg `0.0275` n `20`; unknown avg `2.196` n `1199`
- 4h: commodity avg `0.0598` n `13`; crypto_alt avg `0.8866` n `239`; crypto_major avg `1.0767` n `8`; equity avg `0.4981` n `168`; fx avg `-0.0042` n `6`; index avg `0.0515` n `27`; metal avg `0.0316` n `20`; unknown avg `47.0396` n `1181`
- 24h: commodity avg `0.0831` n `13`; crypto_alt avg `1.8167` n `239`; crypto_major avg `1.0855` n `8`; equity avg `1.1884` n `168`; fx avg `-0.0173` n `6`; index avg `0.0829` n `27`; metal avg `0.1863` n `20`; unknown avg `18.1295` n `1019`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
