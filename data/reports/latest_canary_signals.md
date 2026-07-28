# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T07:22:27.292420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.0845` n `230`; crypto_major avg `-0.001` n `8`; equity avg `0.0924` n `102`; fx avg `0.0014` n `6`; index avg `0.0304` n `25`; metal avg `0.037` n `20`; unknown avg `0.0273` n `774`
- 1h: commodity avg `-0.2149` n `12`; crypto_alt avg `0.1008` n `230`; crypto_major avg `0.1701` n `8`; equity avg `0.3077` n `102`; fx avg `-0.0092` n `6`; index avg `0.0828` n `25`; metal avg `0.0853` n `20`; unknown avg `0.0349` n `774`
- 4h: commodity avg `-0.112` n `12`; crypto_alt avg `0.2101` n `230`; crypto_major avg `-0.0108` n `8`; equity avg `-0.2533` n `102`; fx avg `-0.0342` n `6`; index avg `-0.0204` n `25`; metal avg `0.051` n `20`; unknown avg `0.0067` n `758`
- 24h: commodity avg `-0.5952` n `12`; crypto_alt avg `-3.7879` n `230`; crypto_major avg `-3.6459` n `8`; equity avg `-4.0371` n `102`; fx avg `-0.1688` n `6`; index avg `-0.8089` n `25`; metal avg `-0.4695` n `20`; unknown avg `1158.5356` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
