# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T16:37:35.646914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0585` n `13`; crypto_alt avg `-0.2354` n `235`; crypto_major avg `-0.218` n `8`; equity avg `0.04` n `150`; fx avg `0.0039` n `6`; index avg `-0.0128` n `26`; metal avg `-0.0195` n `20`; unknown avg `2.108` n `1076`
- 1h: commodity avg `0.2302` n `13`; crypto_alt avg `-0.848` n `235`; crypto_major avg `-0.7398` n `8`; equity avg `-0.1549` n `150`; fx avg `-0.0236` n `6`; index avg `-0.0473` n `26`; metal avg `-0.0273` n `20`; unknown avg `1.9212` n `1068`
- 4h: commodity avg `0.4946` n `13`; crypto_alt avg `-0.5004` n `235`; crypto_major avg `-0.5833` n `8`; equity avg `0.1708` n `150`; fx avg `-0.0324` n `6`; index avg `-0.0384` n `26`; metal avg `0.0078` n `20`; unknown avg `5.5255` n `1018`
- 24h: commodity avg `-0.1354` n `13`; crypto_alt avg `0.1785` n `235`; crypto_major avg `0.0545` n `8`; equity avg `0.7608` n `149`; fx avg `0.1141` n `6`; index avg `0.0949` n `26`; metal avg `0.0616` n `20`; unknown avg `381.5429` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1699`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
