# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T13:52:32.616932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0982` n `12`; crypto_alt avg `0.0615` n `230`; crypto_major avg `0.0046` n `8`; equity avg `0.5472` n `114`; fx avg `0.0368` n `6`; index avg `0.0579` n `25`; metal avg `0.0011` n `20`; unknown avg `-0.1119` n `786`
- 1h: commodity avg `-0.0183` n `12`; crypto_alt avg `0.2069` n `230`; crypto_major avg `-0.0277` n `8`; equity avg `-0.0913` n `114`; fx avg `0.0514` n `6`; index avg `-0.0245` n `25`; metal avg `0.092` n `20`; unknown avg `-0.1543` n `786`
- 4h: commodity avg `-0.1529` n `12`; crypto_alt avg `0.2045` n `230`; crypto_major avg `-0.3036` n `8`; equity avg `0.1407` n `114`; fx avg `0.0767` n `6`; index avg `0.0036` n `25`; metal avg `0.1592` n `20`; unknown avg `6.4435` n `786`
- 24h: commodity avg `0.0333` n `12`; crypto_alt avg `-0.7444` n `230`; crypto_major avg `-1.2438` n `8`; equity avg `0.5208` n `114`; fx avg `0.0226` n `6`; index avg `0.1348` n `25`; metal avg `0.0644` n `20`; unknown avg `0.6103` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2018`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
