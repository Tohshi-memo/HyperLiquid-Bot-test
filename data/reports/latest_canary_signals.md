# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T18:22:26.299276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.031` n `13`; crypto_alt avg `-0.1031` n `235`; crypto_major avg `-0.1533` n `8`; equity avg `-0.1973` n `150`; fx avg `-0.0065` n `6`; index avg `-0.0193` n `26`; metal avg `0.0028` n `20`; unknown avg `-0.2358` n `1076`
- 1h: commodity avg `0.0046` n `13`; crypto_alt avg `0.2805` n `235`; crypto_major avg `0.2258` n `8`; equity avg `0.1391` n `150`; fx avg `0.0098` n `6`; index avg `0.0173` n `26`; metal avg `0.078` n `20`; unknown avg `0.0875` n `1074`
- 4h: commodity avg `0.3206` n `13`; crypto_alt avg `-0.2448` n `235`; crypto_major avg `-0.5537` n `8`; equity avg `-0.1791` n `150`; fx avg `0.0263` n `6`; index avg `-0.0585` n `26`; metal avg `0.2518` n `20`; unknown avg `1.0615` n `1040`
- 24h: commodity avg `-0.0585` n `13`; crypto_alt avg `-0.1455` n `235`; crypto_major avg `-0.2114` n `8`; equity avg `0.5915` n `149`; fx avg `0.112` n `6`; index avg `0.0347` n `26`; metal avg `0.0688` n `20`; unknown avg `381.5433` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
