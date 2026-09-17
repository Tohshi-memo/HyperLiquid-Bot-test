# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T10:22:27.880114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1001` n `12`; crypto_alt avg `-0.1425` n `234`; crypto_major avg `-0.1667` n `8`; equity avg `0.0003` n `137`; fx avg `0.0071` n `6`; index avg `0.0067` n `27`; metal avg `-0.0009` n `20`; unknown avg `0.136` n `921`
- 1h: commodity avg `-0.0549` n `12`; crypto_alt avg `-0.5653` n `234`; crypto_major avg `-0.7755` n `8`; equity avg `-0.0268` n `137`; fx avg `0.0297` n `6`; index avg `0.018` n `27`; metal avg `-0.0321` n `20`; unknown avg `0.4174` n `919`
- 4h: commodity avg `-0.0338` n `12`; crypto_alt avg `0.235` n `234`; crypto_major avg `0.0757` n `8`; equity avg `0.8138` n `137`; fx avg `0.0785` n `6`; index avg `0.1383` n `27`; metal avg `0.004` n `20`; unknown avg `-0.1132` n `911`
- 24h: commodity avg `-0.5645` n `12`; crypto_alt avg `2.8927` n `234`; crypto_major avg `1.2494` n `8`; equity avg `1.5119` n `137`; fx avg `0.1161` n `6`; index avg `0.1378` n `27`; metal avg `-0.1896` n `20`; unknown avg `0.4586` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
