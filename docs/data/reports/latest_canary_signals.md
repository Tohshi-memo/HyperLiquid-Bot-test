# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T05:37:17.838861+00:00`
- Correlation status: `ready`
- Asset price records: `522`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.36` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0203` n `12`; crypto_alt avg `0.1638` n `228`; crypto_major avg `0.1563` n `8`; equity avg `0.0983` n `65`; fx avg `-0.0318` n `4`; index avg `0.0308` n `23`; metal avg `0.1768` n `18`; unknown avg `-0.0769` n `358`
- 1h: commodity avg `-0.0981` n `12`; crypto_alt avg `0.7673` n `228`; crypto_major avg `0.3658` n `8`; equity avg `0.2772` n `65`; fx avg `-0.0253` n `4`; index avg `0.0915` n `23`; metal avg `0.2068` n `18`; unknown avg `0.0987` n `358`
- 4h: commodity avg `-0.0628` n `12`; crypto_alt avg `1.025` n `228`; crypto_major avg `0.0411` n `8`; equity avg `0.6482` n `65`; fx avg `0.0123` n `4`; index avg `0.1883` n `23`; metal avg `-0.0436` n `18`; unknown avg `-0.1622` n `358`
- 24h: commodity avg `-1.9213` n `7`; crypto_alt avg `1.4062` n `223`; crypto_major avg `-0.7232` n `7`; equity avg `1.4419` n `47`; fx avg `-0.0687` n `4`; index avg `1.188` n `6`; metal avg `1.6018` n `7`; unknown avg `1.9521` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `518`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1088`, n `518`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `518`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.077`, n `514`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `514`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0696`, n `514`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0694`, n `514`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0684`, n `514`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `518`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0663`, n `518`, weak_sample_signal
