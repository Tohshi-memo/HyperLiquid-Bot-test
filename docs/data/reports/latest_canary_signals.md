# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T09:07:32.129770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0281` n `12`; crypto_alt avg `0.0091` n `228`; crypto_major avg `-0.0149` n `8`; equity avg `0.0512` n `86`; fx avg `-0.0091` n `6`; index avg `0.0053` n `23`; metal avg `0.0298` n `20`; unknown avg `0.0378` n `765`
- 1h: commodity avg `-0.0952` n `12`; crypto_alt avg `-0.1464` n `228`; crypto_major avg `-0.1582` n `8`; equity avg `-0.111` n `86`; fx avg `0.0231` n `6`; index avg `-0.0071` n `23`; metal avg `0.0724` n `20`; unknown avg `0.1463` n `765`
- 4h: commodity avg `0.1196` n `12`; crypto_alt avg `-0.0815` n `228`; crypto_major avg `-0.0512` n `8`; equity avg `0.1093` n `86`; fx avg `-0.0308` n `6`; index avg `0.0108` n `23`; metal avg `0.0799` n `20`; unknown avg `0.2664` n `733`
- 24h: commodity avg `-0.2689` n `12`; crypto_alt avg `-1.1852` n `228`; crypto_major avg `-0.8233` n `8`; equity avg `0.0485` n `86`; fx avg `-0.0288` n `6`; index avg `0.5074` n `23`; metal avg `-1.2846` n `20`; unknown avg `-0.534` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
