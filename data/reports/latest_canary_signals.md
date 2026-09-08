# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T11:37:26.067681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0447` n `12`; crypto_alt avg `0.0163` n `232`; crypto_major avg `-0.0776` n `8`; equity avg `0.0372` n `134`; fx avg `-0.0042` n `6`; index avg `-0.0101` n `26`; metal avg `0.0678` n `20`; unknown avg `0.4508` n `797`
- 1h: commodity avg `0.1452` n `12`; crypto_alt avg `-0.4993` n `232`; crypto_major avg `-0.4758` n `8`; equity avg `0.0326` n `134`; fx avg `0.0105` n `6`; index avg `-0.0269` n `26`; metal avg `0.0594` n `20`; unknown avg `-0.0868` n `795`
- 4h: commodity avg `0.0259` n `12`; crypto_alt avg `0.0028` n `232`; crypto_major avg `-0.1881` n `8`; equity avg `0.157` n `134`; fx avg `0.0116` n `6`; index avg `0.0165` n `26`; metal avg `0.0724` n `20`; unknown avg `1.0843` n `787`
- 24h: commodity avg `0.2453` n `12`; crypto_alt avg `0.3275` n `232`; crypto_major avg `-1.017` n `8`; equity avg `0.0041` n `134`; fx avg `-0.1347` n `6`; index avg `-0.0327` n `26`; metal avg `0.2739` n `20`; unknown avg `7462.841` n `670`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
