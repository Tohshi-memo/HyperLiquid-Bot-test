# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T01:52:32.903254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `0.2399` n `228`; crypto_major avg `0.0639` n `8`; equity avg `0.0153` n `74`; fx avg `0.0085` n `6`; index avg `-0.0086` n `23`; metal avg `-0.0023` n `18`; unknown avg `83.1269` n `645`
- 1h: commodity avg `-0.0303` n `12`; crypto_alt avg `0.4051` n `228`; crypto_major avg `0.2381` n `8`; equity avg `0.062` n `74`; fx avg `-0.01` n `6`; index avg `-0.0031` n `23`; metal avg `0.0044` n `18`; unknown avg `93.9922` n `645`
- 4h: commodity avg `-0.248` n `12`; crypto_alt avg `-0.2046` n `228`; crypto_major avg `-0.0084` n `8`; equity avg `0.0503` n `74`; fx avg `0.0275` n `6`; index avg `-0.126` n `23`; metal avg `-0.6709` n `18`; unknown avg `8.3006` n `644`
- 24h: commodity avg `-0.8476` n `12`; crypto_alt avg `1.374` n `228`; crypto_major avg `1.2666` n `8`; equity avg `0.4402` n `74`; fx avg `-0.0095` n `6`; index avg `0.384` n `23`; metal avg `0.2298` n `18`; unknown avg `0.1826` n `611`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
