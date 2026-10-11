# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T04:22:25.600695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `13`; crypto_alt avg `0.3095` n `235`; crypto_major avg `0.1546` n `8`; equity avg `0.037` n `150`; fx avg `0.0` n `6`; index avg `0.0078` n `26`; metal avg `0.0025` n `20`; unknown avg `0.0247` n `1117`
- 1h: commodity avg `-0.006` n `13`; crypto_alt avg `-0.2121` n `235`; crypto_major avg `-0.1586` n `8`; equity avg `-0.0423` n `150`; fx avg `-0.0052` n `6`; index avg `-0.0071` n `26`; metal avg `-0.0028` n `20`; unknown avg `0.1548` n `1109`
- 4h: commodity avg `0.0926` n `13`; crypto_alt avg `-0.8173` n `235`; crypto_major avg `-0.4123` n `8`; equity avg `-0.0981` n `150`; fx avg `0.0014` n `6`; index avg `-0.0173` n `26`; metal avg `0.0011` n `20`; unknown avg `-0.3656` n `1109`
- 24h: commodity avg `0.1862` n `13`; crypto_alt avg `0.2721` n `235`; crypto_major avg `-0.0431` n `8`; equity avg `-0.0536` n `150`; fx avg `-0.0123` n `6`; index avg `-0.032` n `26`; metal avg `-0.0098` n `20`; unknown avg `0.2033` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
