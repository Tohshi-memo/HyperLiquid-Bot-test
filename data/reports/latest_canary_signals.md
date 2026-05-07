# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T20:44:07.192069+00:00`
- Correlation status: `ready`
- Asset price records: `582`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.457` n `12`; crypto_alt avg `-0.2415` n `228`; crypto_major avg `-0.1703` n `8`; equity avg `-0.0348` n `65`; fx avg `-0.0042` n `5`; index avg `-0.021` n `23`; metal avg `-0.307` n `18`; unknown avg `-0.0109` n `365`
- 1h: commodity avg `0.3798` n `12`; crypto_alt avg `-0.0637` n `228`; crypto_major avg `-0.1081` n `8`; equity avg `0.2095` n `65`; fx avg `-0.004` n `5`; index avg `0.0291` n `23`; metal avg `-0.0882` n `18`; unknown avg `0.1386` n `365`
- 4h: commodity avg `0.7297` n `12`; crypto_alt avg `0.8918` n `228`; crypto_major avg `0.0341` n `8`; equity avg `-0.3073` n `65`; fx avg `-0.0161` n `5`; index avg `-0.3029` n `23`; metal avg `-0.5449` n `18`; unknown avg `-0.3217` n `365`
- 24h: commodity avg `0.7091` n `12`; crypto_alt avg `1.3779` n `228`; crypto_major avg `-1.8497` n `8`; equity avg `-1.3738` n `65`; fx avg `0.1771` n `5`; index avg `-0.8469` n `23`; metal avg `0.0898` n `18`; unknown avg `-0.3814` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1404`, n `578`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `578`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `578`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0976`, n `578`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `574`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `574`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0935`, n `574`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0891`, n `574`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.082`, n `574`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0766`, n `574`, weak_sample_signal
