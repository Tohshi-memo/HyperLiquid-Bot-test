# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T03:07:24.517119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `-0.1146` n `231`; crypto_major avg `-0.0717` n `8`; equity avg `-0.0385` n `122`; fx avg `0.0084` n `6`; index avg `-0.0046` n `25`; metal avg `-0.0819` n `20`; unknown avg `0.0985` n `797`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `0.5519` n `231`; crypto_major avg `0.3939` n `8`; equity avg `0.607` n `122`; fx avg `0.0575` n `6`; index avg `0.1332` n `25`; metal avg `-0.0345` n `20`; unknown avg `0.6945` n `797`
- 4h: commodity avg `-0.107` n `12`; crypto_alt avg `0.6809` n `231`; crypto_major avg `0.2824` n `8`; equity avg `-0.117` n `122`; fx avg `0.0125` n `6`; index avg `0.0165` n `25`; metal avg `0.0419` n `20`; unknown avg `0.5803` n `795`
- 24h: commodity avg `-0.863` n `12`; crypto_alt avg `-2.588` n `231`; crypto_major avg `-2.8297` n `8`; equity avg `1.6199` n `122`; fx avg `0.0397` n `6`; index avg `0.2449` n `25`; metal avg `0.3053` n `20`; unknown avg `0.1483` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
