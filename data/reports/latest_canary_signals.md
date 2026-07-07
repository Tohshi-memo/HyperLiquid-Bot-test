# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T07:52:28.430717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0518` n `12`; crypto_alt avg `0.0484` n `229`; crypto_major avg `0.0142` n `8`; equity avg `-0.0338` n `91`; fx avg `-0.0445` n `6`; index avg `-0.0111` n `25`; metal avg `-0.0555` n `20`; unknown avg `-0.0492` n `763`
- 1h: commodity avg `0.0967` n `12`; crypto_alt avg `-0.223` n `229`; crypto_major avg `-0.262` n `8`; equity avg `-0.0711` n `91`; fx avg `-0.0686` n `6`; index avg `-0.0061` n `25`; metal avg `-0.0269` n `20`; unknown avg `-0.1431` n `763`
- 4h: commodity avg `0.2979` n `12`; crypto_alt avg `0.1611` n `229`; crypto_major avg `0.1548` n `8`; equity avg `0.3601` n `91`; fx avg `-0.029` n `6`; index avg `0.0747` n `25`; metal avg `-0.0109` n `20`; unknown avg `6.6884` n `745`
- 24h: commodity avg `0.6303` n `12`; crypto_alt avg `0.2478` n `229`; crypto_major avg `-0.5318` n `8`; equity avg `-1.3591` n `90`; fx avg `-0.0733` n `6`; index avg `-0.3532` n `25`; metal avg `-0.5676` n `20`; unknown avg `-0.483` n `743`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
