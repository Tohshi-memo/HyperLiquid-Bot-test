# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T15:22:37.444797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0301` n `12`; crypto_alt avg `-0.1189` n `232`; crypto_major avg `-0.1092` n `8`; equity avg `0.0891` n `128`; fx avg `0.0067` n `6`; index avg `-0.0114` n `26`; metal avg `0.0095` n `20`; unknown avg `0.0699` n `794`
- 1h: commodity avg `0.0698` n `12`; crypto_alt avg `0.2986` n `232`; crypto_major avg `0.4822` n `8`; equity avg `0.1123` n `128`; fx avg `0.0274` n `6`; index avg `-0.0178` n `26`; metal avg `0.0316` n `20`; unknown avg `0.7043` n `792`
- 4h: commodity avg `-0.0985` n `12`; crypto_alt avg `-0.4589` n `232`; crypto_major avg `-0.2654` n `8`; equity avg `0.0125` n `128`; fx avg `0.0649` n `6`; index avg `-0.0986` n `26`; metal avg `-0.3325` n `20`; unknown avg `0.5982` n `790`
- 24h: commodity avg `0.5679` n `12`; crypto_alt avg `-1.1376` n `231`; crypto_major avg `-1.6183` n `8`; equity avg `-0.4586` n `128`; fx avg `-0.0783` n `6`; index avg `-0.1861` n `26`; metal avg `-0.4863` n `20`; unknown avg `0.5056` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
