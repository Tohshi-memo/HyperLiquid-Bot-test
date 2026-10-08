# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T05:52:32.836024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `13`; crypto_alt avg `-0.6565` n `235`; crypto_major avg `-0.371` n `8`; equity avg `-0.2263` n `150`; fx avg `-0.0099` n `6`; index avg `-0.0385` n `26`; metal avg `-0.1017` n `20`; unknown avg `0.4721` n `1077`
- 1h: commodity avg `0.0616` n `13`; crypto_alt avg `0.0768` n `235`; crypto_major avg `0.057` n `8`; equity avg `-0.2412` n `150`; fx avg `-0.0161` n `6`; index avg `-0.0337` n `26`; metal avg `-0.1518` n `20`; unknown avg `3.7146` n `1075`
- 4h: commodity avg `0.1392` n `13`; crypto_alt avg `-0.9089` n `235`; crypto_major avg `-0.9455` n `8`; equity avg `-0.7839` n `150`; fx avg `0.0193` n `6`; index avg `-0.0995` n `26`; metal avg `-0.1663` n `20`; unknown avg `-0.1549` n `1069`
- 24h: commodity avg `0.4933` n `13`; crypto_alt avg `-1.3945` n `235`; crypto_major avg `-2.4581` n `8`; equity avg `-1.602` n `150`; fx avg `-0.1247` n `6`; index avg `-0.2546` n `26`; metal avg `-0.2968` n `20`; unknown avg `246.9815` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
