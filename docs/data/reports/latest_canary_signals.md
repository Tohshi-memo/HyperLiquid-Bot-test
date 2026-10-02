# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T23:37:37.064169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `13`; crypto_alt avg `0.2625` n `235`; crypto_major avg `0.0874` n `8`; equity avg `0.0181` n `143`; fx avg `-0.0037` n `6`; index avg `0.001` n `26`; metal avg `-0.006` n `20`; unknown avg `-0.0425` n `984`
- 1h: commodity avg `-0.0314` n `13`; crypto_alt avg `0.6304` n `235`; crypto_major avg `0.2414` n `8`; equity avg `0.0261` n `143`; fx avg `0.0029` n `6`; index avg `0.0057` n `26`; metal avg `0.006` n `20`; unknown avg `-0.2382` n `982`
- 4h: commodity avg `0.2781` n `13`; crypto_alt avg `1.1327` n `235`; crypto_major avg `0.6282` n `8`; equity avg `-0.087` n `143`; fx avg `-0.0251` n `6`; index avg `-0.0195` n `26`; metal avg `-0.0323` n `20`; unknown avg `-0.0954` n `906`
- 24h: commodity avg `0.1395` n `13`; crypto_alt avg `-0.3869` n `235`; crypto_major avg `-0.4037` n `8`; equity avg `0.6981` n `142`; fx avg `-0.137` n `6`; index avg `0.297` n `26`; metal avg `-0.2583` n `20`; unknown avg `-0.5912` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
