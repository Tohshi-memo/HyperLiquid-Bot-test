# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T04:52:15.449564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `0.2432` n `228`; crypto_major avg `0.2708` n `8`; equity avg `0.0604` n `66`; fx avg `0.0044` n `5`; index avg `0.0077` n `23`; metal avg `-0.055` n `18`; unknown avg `-0.6026` n `383`
- 1h: commodity avg `0.0496` n `12`; crypto_alt avg `0.3445` n `228`; crypto_major avg `0.2689` n `8`; equity avg `-0.0329` n `66`; fx avg `0.0068` n `5`; index avg `0.0067` n `23`; metal avg `0.1658` n `18`; unknown avg `-0.6594` n `383`
- 4h: commodity avg `0.2363` n `12`; crypto_alt avg `0.5749` n `228`; crypto_major avg `-0.05` n `8`; equity avg `0.6988` n `66`; fx avg `0.0636` n `5`; index avg `0.2513` n `23`; metal avg `0.6618` n `18`; unknown avg `-0.7814` n `383`
- 24h: commodity avg `2.7221` n `12`; crypto_alt avg `-10.7361` n `228`; crypto_major avg `-3.1909` n `8`; equity avg `-3.079` n `65`; fx avg `-0.0624` n `5`; index avg `-1.7692` n `23`; metal avg `-6.1441` n `18`; unknown avg `550.0818` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
