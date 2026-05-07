# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T15:07:31.410158+00:00`
- Correlation status: `ready`
- Asset price records: `560`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2007` n `12`; crypto_alt avg `-0.2101` n `228`; crypto_major avg `0.0085` n `8`; equity avg `-0.2948` n `65`; fx avg `0.0034` n `5`; index avg `0.0283` n `23`; metal avg `-0.0687` n `18`; unknown avg `0.0344` n `365`
- 1h: commodity avg `0.7549` n `12`; crypto_alt avg `-0.5588` n `228`; crypto_major avg `-0.2615` n `8`; equity avg `-0.0017` n `65`; fx avg `-0.0042` n `5`; index avg `0.2843` n `23`; metal avg `0.2883` n `18`; unknown avg `-0.0888` n `365`
- 4h: commodity avg `-0.073` n `12`; crypto_alt avg `-0.8062` n `228`; crypto_major avg `-1.0264` n `8`; equity avg `-0.6468` n `65`; fx avg `-0.0141` n `5`; index avg `-0.2123` n `23`; metal avg `0.4081` n `18`; unknown avg `-0.4158` n `365`
- 24h: commodity avg `-0.8314` n `12`; crypto_alt avg `0.3017` n `228`; crypto_major avg `-1.7106` n `8`; equity avg `0.7877` n `65`; fx avg `0.1132` n `5`; index avg `0.4123` n `23`; metal avg `1.8213` n `18`; unknown avg `-0.0213` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1326`, n `556`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1233`, n `556`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1046`, n `556`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0999`, n `556`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `556`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0793`, n `552`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.078`, n `552`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.078`, n `552`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `556`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0748`, n `552`, weak_sample_signal
