# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T03:52:30.175508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0231` n `12`; crypto_alt avg `-0.0745` n `232`; crypto_major avg `-0.0964` n `8`; equity avg `0.0513` n `130`; fx avg `0.0252` n `6`; index avg `0.007` n `26`; metal avg `0.0663` n `20`; unknown avg `0.3347` n `792`
- 1h: commodity avg `-0.0181` n `12`; crypto_alt avg `0.4783` n `232`; crypto_major avg `0.4115` n `8`; equity avg `0.2264` n `130`; fx avg `0.0237` n `6`; index avg `0.0323` n `26`; metal avg `0.0704` n `20`; unknown avg `0.2572` n `790`
- 4h: commodity avg `0.0458` n `12`; crypto_alt avg `0.8517` n `232`; crypto_major avg `0.3539` n `8`; equity avg `0.1089` n `130`; fx avg `0.0457` n `6`; index avg `0.0271` n `26`; metal avg `0.0514` n `20`; unknown avg `0.335` n `790`
- 24h: commodity avg `0.3814` n `12`; crypto_alt avg `1.7981` n `232`; crypto_major avg `1.7865` n `8`; equity avg `1.3744` n `130`; fx avg `0.0194` n `6`; index avg `0.1458` n `26`; metal avg `0.0592` n `20`; unknown avg `0.165` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0448`, n `668`, weak_sample_signal
