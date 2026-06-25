# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T07:52:30.598277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7382` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0716` n `12`; crypto_alt avg `0.07` n `228`; crypto_major avg `-0.0957` n `8`; equity avg `-0.0048` n `86`; fx avg `-0.0071` n `6`; index avg `-0.0045` n `23`; metal avg `-0.0324` n `20`; unknown avg `-0.0168` n `765`
- 1h: commodity avg `0.1702` n `12`; crypto_alt avg `-0.0742` n `228`; crypto_major avg `-0.0977` n `8`; equity avg `0.1175` n `86`; fx avg `-0.0047` n `6`; index avg `0.0085` n `23`; metal avg `0.0196` n `20`; unknown avg `-0.0145` n `749`
- 4h: commodity avg `0.2252` n `12`; crypto_alt avg `1.0352` n `228`; crypto_major avg `1.5097` n `8`; equity avg `0.4841` n `86`; fx avg `-0.0561` n `6`; index avg `0.0665` n `23`; metal avg `-0.2285` n `20`; unknown avg `0.1053` n `733`
- 24h: commodity avg `-0.2412` n `12`; crypto_alt avg `-0.8772` n `228`; crypto_major avg `-0.4543` n `8`; equity avg `0.1385` n `86`; fx avg `-0.0451` n `6`; index avg `0.5305` n `23`; metal avg `-1.7583` n `20`; unknown avg `-0.7202` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
